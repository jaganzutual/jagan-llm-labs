import torch

from implementations.gpt.softmax import my_softmax


def test_softmax_sums_to_one():
    z = torch.tensor([[0.0, 1.0, 0.0]])
    out = my_softmax(z, dim=-1)
    assert out.shape == (1, 3)
    assert torch.allclose(out.sum(dim=-1), torch.tensor([1.0]), atol=1e-5)


def test_softmax_known_values():
    z = torch.tensor([[0.0, 1.0, 0.0]])
    out = my_softmax(z, dim=-1)
    expected = torch.tensor([[0.2119, 0.5761, 0.2119]])
    assert torch.allclose(out, expected, atol=1e-3)


def test_softmax_bigger_input_bigger_weight():
    z = torch.tensor([[2.0, 1.0, 0.0]])
    out = my_softmax(z, dim=-1)
    assert out[0, 0] > out[0, 1] > out[0, 2]
