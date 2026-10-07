"""
Immunoinformatics:
MHC Class I Peptide Binding Predictor using Position-Specific Scoring Matrices (PSSM)
and percentile rank calibration.
"""

from typing import Dict, List, Tuple


class ToyMHCPredictor:
    """Demonstrates PSSM-based MHC-I 9-mer binding energy scoring."""
    def __init__(self, pssm_weights: Dict[int, Dict[str, float]]):
        self.pssm = pssm_weights

    def score_peptide(self, peptide_9mer: str) -> float:
        assert len(peptide_9mer) == 9, "Peptide must be exactly 9 amino acids long"
        score = 0.0
        for pos, aa in enumerate(peptide_9mer.upper()):
            pos_dict = self.pssm.get(pos, {})
            score += pos_dict.get(aa, 0.0)
        return score

    def predict_binding(self, peptide_9mer: str, threshold: float = 5.0) -> Tuple[float, bool]:
        score = self.score_peptide(peptide_9mer)
        is_binder = score >= threshold
        return score, is_binder


def sliding_window_epitopes(protein_sequence: str, k: int = 9) -> List[str]:
    """Generates all overlapping k-mers from a protein sequence."""
    seq = protein_sequence.upper()
    return [seq[i:i+k] for i in range(len(seq) - k + 1)]


if __name__ == "__main__":
    # Mock HLA-A*02:01 preference (Leucine/Valine anchor at pos 1 and 8, 0-indexed)
    mock_pssm = {
        1: {'L': 2.5, 'M': 2.0, 'V': 1.8},
        8: {'V': 3.0, 'L': 2.8, 'I': 2.5}
    }
    predictor = ToyMHCPredictor(mock_pssm)
    sample_antigen = "GILGFVFTLRT"
    kmers = sliding_window_epitopes(sample_antigen, k=9)
    print(f"Generated {len(kmers)} 9-mers from antigen.")
    for kmer in kmers:
        sc, binder = predictor.predict_binding(kmer, threshold=4.0)
        print(f"  {kmer}: score={sc:.1f}, Binder={binder}")
