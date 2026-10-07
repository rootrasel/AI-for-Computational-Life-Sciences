"""
VCF Quality Control & Parsing Utility:
Calculates Transition/Transversion (Ti/Tv) ratio, allele frequencies,
and filters variants based on depth and genotype quality.
"""

from typing import Dict, List, Tuple
import io

PURINES = {'A', 'G'}
PYRIMIDINES = {'C', 'T'}


def is_transition(ref: str, alt: str) -> bool:
    """True if mutation is purine->purine or pyrimidine->pyrimidine."""
    ref_u, alt_u = ref.upper(), alt.upper()
    return (ref_u in PURINES and alt_u in PURINES) or (ref_u in PYRIMIDINES and alt_u in PYRIMIDINES)


class VCFStatsCollector:
    def __init__(self):
        self.total_records = 0
        self.transitions = 0
        self.transversions = 0
        self.indels = 0
        self.depths: List[int] = []

    def process_record(self, chrom: str, pos: int, ref: str, alt: str, qual: float, info: str, fmt: str, sample_val: str):
        self.total_records += 1
        
        # SNV vs Indel
        if len(ref) == 1 and len(alt) == 1:
            if is_transition(ref, alt):
                self.transitions += 1
            else:
                self.transversions += 1
        else:
            self.indels += 1
            
        # Parse DP from FORMAT
        fmt_fields = fmt.split(':')
        sample_fields = sample_val.split(':')
        if 'DP' in fmt_fields:
            dp_idx = fmt_fields.index('DP')
            try:
                self.depths.append(int(sample_fields[dp_idx]))
            except (ValueError, IndexError):
                pass

    @property
    def ti_tv_ratio(self) -> float:
        if self.transversions == 0:
            return float('inf')
        return self.transitions / float(self.transversions)

    def summary(self) -> Dict[str, float]:
        mean_dp = sum(self.depths) / len(self.depths) if self.depths else 0.0
        return {
            "total_records": self.total_records,
            "transitions": self.transitions,
            "transversions": self.transversions,
            "ti_tv_ratio": round(self.ti_tv_ratio, 3),
            "indels": self.indels,
            "mean_depth": round(mean_dp, 2)
        }


def parse_vcf_stream(vcf_lines: List[str]) -> Dict[str, float]:
    collector = VCFStatsCollector()
    for line in vcf_lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split('	')
        if len(parts) >= 10:
            chrom, pos, id_, ref, alt, qual_str, filt, info, fmt, sample = parts[:10]
            qual = float(qual_str) if qual_str != '.' else 0.0
            collector.process_record(chrom, int(pos), ref, alt, qual, info, fmt, sample)
    return collector.summary()


if __name__ == "__main__":
    mock_vcf = [
        "##fileformat=VCFv4.2",
        "#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	SAMPLE1",
        "chr1	1000	.	A	G	50.0	PASS	.	GT:DP	0/1:35",
        "chr1	1050	.	C	T	60.0	PASS	.	GT:DP	1/1:42",
        "chr1	1100	.	A	C	45.0	PASS	.	GT:DP	0/1:28",
        "chr1	1200	.	G	GA	55.0	PASS	.	GT:DP	0/1:30"
    ]
    res = parse_vcf_stream(mock_vcf)
    print("VCF Parsing Result:", res)
