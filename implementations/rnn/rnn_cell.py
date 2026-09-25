import torch
import torch.nn as nn

torch.manual_seed(2810)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



class RNNCell(nn.Module):
    def __init__(self,input_size,hidden_size):
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.input_to_hidden = nn.Linear(input_size, hidden_size)
        self.hidden_to_hidden = nn.Linear(hidden_size, hidden_size, bias=False)

    def forward(self, x, h):
        return torch.tanh(self.input_to_hidden(x) + self.hidden_to_hidden(h))


cell = RNNCell(input_size=10, hidden_size=20)
