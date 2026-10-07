import numpy as np
from sklearn.metrics import roc_auc_score, average_precision_score, f1_score


def evaluate_predictions(y_true: np.ndarray, y_probs: np.ndarray) -> dict:
    roc_auc = roc_auc_score(y_true, y_probs)
    pr_auc = average_precision_score(y_true, y_probs)
    preds = (y_probs >= 0.5).astype(int)
    f1 = f1_score(y_true, preds)
    return {
        "ROC-AUC": round(float(roc_auc), 4),
        "PR-AUC": round(float(pr_auc), 4),
        "F1-Score": round(float(f1), 4)
    }
