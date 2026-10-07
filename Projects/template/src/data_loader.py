import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from typing import Tuple


class BiologicalDataset(Dataset):
    def __init__(self, features: np.ndarray, labels: np.ndarray):
        self.features = torch.tensor(features, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.float32)

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        return self.features[idx], self.labels[idx]


def get_dataloaders(
    batch_size: int = 32
) -> Tuple[DataLoader, DataLoader, DataLoader]:
    np.random.seed(42)
    X = np.random.normal(size=(500, 64))
    y = (X[:, 0] * 2.0 + X[:, 1] > 0).astype(float)
    
    train_ds = BiologicalDataset(X[:350], y[:350])
    val_ds = BiologicalDataset(X[350:420], y[350:420])
    test_ds = BiologicalDataset(X[420:], y[420:])
    
    return (
        DataLoader(train_ds, batch_size=batch_size, shuffle=True),
        DataLoader(val_ds, batch_size=batch_size, shuffle=False),
        DataLoader(test_ds, batch_size=batch_size, shuffle=False)
    )
