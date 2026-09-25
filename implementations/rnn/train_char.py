"""
Train a tiny character-level language model on Shakespeare.

Architecture: Embedding -> RNN (our own) -> Linear -> predict next char.
"""

from pathlib import Path

import torch
import torch.nn as nn

from implementations.rnn.rnn_unrolled import RNNUnrolled
