"""
Biomedical Knowledge Graph:
Subgraph extractor, TransE score function,
and link prediction ranking evaluator.
"""

from typing import Dict, List, Tuple
import numpy as np


class TransEEvaluator:
    """Evaluates TransE score: f(h, r, t) = - || h + r - t ||_2"""
    def __init__(self, embedding_dim: int, n_entities: int, n_relations: int):
        self.embedding_dim = embedding_dim
        # Normalized random embeddings
        self.ent_embeddings = np.random.normal(size=(n_entities, embedding_dim))
        self.ent_embeddings /= np.linalg.norm(self.ent_embeddings, axis=1, keepdims=True)
        self.rel_embeddings = np.random.normal(size=(n_relations, embedding_dim))

    def score_triple(self, head_id: int, rel_id: int, tail_id: int) -> float:
        h = self.ent_embeddings[head_id]
        r = self.rel_embeddings[rel_id]
        t = self.ent_embeddings[tail_id]
        return -float(np.linalg.norm(h + r - t, ord=2))

    def evaluate_tail_ranking(self, head_id: int, rel_id: int, true_tail_id: int) -> int:
        """Computes 1-indexed rank of the true tail among all entities."""
        h = self.ent_embeddings[head_id]
        r = self.rel_embeddings[rel_id]
        # Distances to all entities
        diff = (h + r)[np.newaxis, :] - self.ent_embeddings
        scores = -np.linalg.norm(diff, axis=1)
        ranks = np.argsort(scores)[::-1]
        rank = int(np.where(ranks == true_tail_id)[0][0]) + 1
        return rank


if __name__ == "__main__":
    np.random.seed(42)
    evaluator = TransEEvaluator(embedding_dim=16, n_entities=100, n_relations=10)
    sc = evaluator.score_triple(head_id=5, rel_id=2, tail_id=12)
    print(f"TransE triple score: {sc:.3f}")
    rank = evaluator.evaluate_tail_ranking(head_id=5, rel_id=2, true_tail_id=12)
    print(f"Tail entity rank: {rank} / 100")
