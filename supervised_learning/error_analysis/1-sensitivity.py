itivity"""

import numpy as np


def sensitivity(confusion):
    """Calculating the sensitivity for each class in a confusion matrix"""
    return np.diag(confusion) / np.sum(confusion, axis=1:)
