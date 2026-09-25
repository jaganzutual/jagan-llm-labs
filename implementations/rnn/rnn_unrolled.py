import torch
import torch.nn as nn
from implementations.rnn.rnn_cell import RNNCell

class RNNUnrolled(nn.Module):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.cell = RNNCell(input_size,hidden_size)

    def forward(self,x):


        batch_size, sequence_length, _ = x.shape

        h = torch.zeros(
            batch_size,
            self.cell.hidden_size,
            device=x.device
        )

        outputs = []

        for t in range(sequence_length):

            x_t = x[:, t, :]

            # Update hidden state
            h = self.cell(x_t, h)

            # Store hidden state
            outputs.append(h)

        # [batch, sequence, hidden]
        outputs = torch.stack(outputs, dim=1)

        return outputs
