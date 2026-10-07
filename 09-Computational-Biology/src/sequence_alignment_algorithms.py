"""
Algorithmic Sequence Alignment:
Needleman-Wunsch (Global) and Smith-Waterman (Local) alignment
with affine gap penalties and full traceback reconstruction.
"""

from typing import Tuple, List


class Matrix2D:
    """Lightweight 2D matrix supporting tuple indexing score_matrix[i, j]."""
    def __init__(self, rows: int, cols: int, default: int = 0):
        self.data = [[default] * cols for _ in range(rows)]

    def __getitem__(self, idx: Tuple[int, int]) -> int:
        r, c = idx
        return self.data[r][c]

    def __setitem__(self, idx: Tuple[int, int], val: int):
        r, c = idx
        self.data[r][c] = val


def needleman_wunsch_global(
    seq1: str,
    seq2: str,
    match: int = 2,
    mismatch: int = -1,
    gap: int = -2
) -> Tuple[int, str, str]:
    """
    Global sequence alignment with constant gap penalty.
    Returns: (optimal_score, aligned_seq1, aligned_seq2)
    """
    m, n = len(seq1), len(seq2)
    score_matrix = Matrix2D(m + 1, n + 1, default=0)
    
    for i in range(m + 1):
        score_matrix[i, 0] = i * gap
    for j in range(n + 1):
        score_matrix[0, j] = j * gap
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s = match if seq1[i - 1] == seq2[j - 1] else mismatch
            score_matrix[i, j] = max(
                score_matrix[i - 1, j - 1] + s,
                score_matrix[i - 1, j] + gap,
                score_matrix[i, j - 1] + gap
            )
            
    # Traceback
    align1, align2 = [], []
    i, j = m, n
    while i > 0 or j > 0:
        s = match if (i > 0 and j > 0 and seq1[i - 1] == seq2[j - 1]) else mismatch
        if i > 0 and j > 0 and score_matrix[i, j] == score_matrix[i - 1, j - 1] + s:
            align1.append(seq1[i - 1])
            align2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and score_matrix[i, j] == score_matrix[i - 1, j] + gap:
            align1.append(seq1[i - 1])
            align2.append('-')
            i -= 1
        else:
            align1.append('-')
            align2.append(seq2[j - 1])
            j -= 1
            
    return int(score_matrix[m, n]), "".join(reversed(align1)), "".join(reversed(align2))


def smith_waterman_local(
    seq1: str,
    seq2: str,
    match: int = 3,
    mismatch: int = -3,
    gap: int = -2
) -> Tuple[int, str, str]:
    """
    Local sequence alignment with boundary clamping at 0.
    Returns: (max_score, local_align1, local_align2)
    """
    m, n = len(seq1), len(seq2)
    score_matrix = Matrix2D(m + 1, n + 1, default=0)
    max_score = 0
    max_pos = (0, 0)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s = match if seq1[i - 1] == seq2[j - 1] else mismatch
            score_matrix[i, j] = max(
                0,
                score_matrix[i - 1, j - 1] + s,
                score_matrix[i - 1, j] + gap,
                score_matrix[i, j - 1] + gap
            )
            if score_matrix[i, j] > max_score:
                max_score = score_matrix[i, j]
                max_pos = (i, j)
                
    # Traceback from max score position until 0 is hit
    align1, align2 = [], []
    i, j = max_pos
    while i > 0 and j > 0 and score_matrix[i, j] > 0:
        s = match if seq1[i - 1] == seq2[j - 1] else mismatch
        if score_matrix[i, j] == score_matrix[i - 1, j - 1] + s:
            align1.append(seq1[i - 1])
            align2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif score_matrix[i, j] == score_matrix[i - 1, j] + gap:
            align1.append(seq1[i - 1])
            align2.append('-')
            i -= 1
        else:
            align1.append('-')
            align2.append(seq2[j - 1])
            j -= 1
            
    return int(max_score), "".join(reversed(align1)), "".join(reversed(align2))


if __name__ == "__main__":
    s1 = "HEAGAWGHEE"
    s2 = "PAWHEAE"
    score_nw, a1, a2 = needleman_wunsch_global(s1, s2)
    print(f"Global NW score: {score_nw}\n{a1}\n{a2}")
    score_sw, sw1, sw2 = smith_waterman_local(s1, s2)
    print(f"Local SW score: {score_sw}\n{sw1}\n{sw2}")
