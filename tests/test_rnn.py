import torch
import torch.nn as nn

from implementations.rnn.rnn_cell import RNNCell
from implementations.rnn.rnn_unrolled import RNNUnrolled


def test_rnn_cell_output_shape():
    torch.manual_seed(0)
    cell = RNNCell(input_size=10, hidden_size=20)
    x = torch.randn(4, 10)
    h = torch.zeros(4, 20)
    out = cell(x, h)
    assert out.shape == (4, 20)


def test_rnn_cell_output_bounded_by_tanh():
    torch.manual_seed(0)
    cell = RNNCell(input_size=10, hidden_size=20)
    x = torch.randn(4, 10)
    h = torch.randn(4, 20)
    out = cell(x, h)
    assert (out.abs() <= 1.0 + 1e-6).all()


def test_rnn_cell_gradient_flows():
    torch.manual_seed(0)
    cell = RNNCell(input_size=10, hidden_size=20)
    x = torch.randn(2, 10, requires_grad=True)
    h = torch.zeros(2, 20)
    out = cell(x, h)
    out.sum().backward()
    assert x.grad is not None
    assert x.grad.shape == x.shape


def test_rnn_unrolled_output_shape():
    torch.manual_seed(0)
    model = RNNUnrolled(input_size=10, hidden_size=20)
    x = torch.randn(4, 5, 10)
    out = model(x)
    assert out.shape == (4, 5, 20)


def test_rnn_unrolled_hidden_propagates():
    torch.manual_seed(0)
    model = RNNUnrolled(input_size=10, hidden_size=20)
    x = torch.randn(2, 5, 10)
    out = model(x)
    h_final = out[:, -1, :]
    assert h_final.shape == (2, 20)


def test_rnn_unrolled_outputs_bounded_by_tanh():
    torch.manual_seed(0)
    model = RNNUnrolled(input_size=10, hidden_size=20)
    x = torch.randn(3, 5, 10)
    out = model(x)
    assert (out.abs() <= 1.0 + 1e-6).all()


def test_rnn_unrolled_matches_torch_nn_RNN():
    torch.manual_seed(0)
    my_model = RNNUnrolled(input_size=10, hidden_size=20)
    torch.manual_seed(0)
    torch_model = nn.RNN(input_size=10, hidden_size=20, nonlinearity="tanh")

    my_model.cell.input_to_hidden.weight.data.copy_(torch_model.weight_ih_l0.data)
    my_model.cell.input_to_hidden.bias.data.copy_(
        torch_model.bias_ih_l0.data + torch_model.bias_hh_l0.data
    )
    my_model.cell.hidden_to_hidden.weight.data.copy_(torch_model.weight_hh_l0.data)

    x = torch.randn(2, 3, 10)
    my_out = my_model(x)
    torch_out, _ = torch_model(x.transpose(0, 1))
    torch_out = torch_out.transpose(0, 1)

    assert torch.allclose(my_out, torch_out, atol=1e-5)
