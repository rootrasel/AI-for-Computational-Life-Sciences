import torch
import torch.nn as nn
from src.model import BiologicalPredictorNet
from src.data_loader import get_dataloaders
from src.utils import seed_everything


def train_pipeline(epochs: int = 5):
    seed_everything(42)
    train_loader, val_loader, _ = get_dataloaders(batch_size=32)
    model = BiologicalPredictorNet(in_dim=64, hidden_dim=128, out_dim=1)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)
    criterion = nn.BCEWithLogitsLoss()

    for epoch in range(1, epochs + 1):
        model.train()
        total_loss = 0.0
        for X_b, y_b in train_loader:
            optimizer.zero_grad()
            preds = model(X_b)
            loss = criterion(preds, y_b)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch}/{epochs} - Loss: {total_loss / len(train_loader):.4f}")


if __name__ == "__main__":
    train_pipeline()
