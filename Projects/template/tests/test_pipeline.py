import torch
from src.model import BiologicalPredictorNet


def test_model_forward_shape():
    model = BiologicalPredictorNet(in_dim=64, hidden_dim=128, out_dim=1)
    dummy_input = torch.randn(16, 64)
    out = model(dummy_input)
    assert out.shape == (16,), f"Expected shape (16,), got {out.shape}"
