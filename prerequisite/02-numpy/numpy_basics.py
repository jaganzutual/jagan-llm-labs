# Stage 2 — NumPy Basics
#
# Run as a regular .py file. Each task is a small function + a test block.
# Fill in the `...` body of each function so the asserts pass.


import numpy as np


# TASK 1 - Create basic arrays
#
# Write make_arrays(): return a dict with these five keys:
#   "zeros" : np.zeros((3, 4))                  -> shape (3, 4)
#   "ones"  : np.ones((2, 3, 4))                -> shape (2, 3, 4)
#   "arange": np.arange(0, 10, 2)               -> [0, 2, 4, 6, 8]
#   "random": np.random.randn(3, 3)             -> 3x3 random floats
#   "from_list": np.array([[1, 2], [3, 4]])     -> 2x2 from a Python list
#
# Why it matters: every tensor you'll ever see in PyTorch is just
# one of these construction calls under the hood.


def make_arrays():
    ...


result = make_arrays()
assert result["zeros"].shape == (3, 4)
assert result["ones"].shape == (2, 3, 4)
assert np.array_equal(result["arange"], np.array([0, 2, 4, 6, 8]))
assert result["random"].shape == (3, 3)
assert np.array_equal(result["from_list"], np.array([[1, 2], [3, 4]]))
print("Task 1 passed")


# TASK 2 - Shape inspection
#
# Write describe(x): return a dict with:
#   "shape" : tuple, x.shape
#   "dtype" : numpy dtype, x.dtype
#   "ndim"  : int, number of dimensions
#
# These three attributes show up in EVERY error message PyTorch
# will ever throw at you. Get used to reading them.


def describe(x):
    ...


info = describe(np.array([[1.0, 2.0], [3.0, 4.0]]))
assert info["shape"] == (2, 2)
assert info["dtype"] == np.float64
assert info["ndim"] == 2
print("Task 2 passed")


# TASK 3 - Indexing and slicing
#
# Write slice_demo(x): x is shape (4, 5). Return a dict with:
#   "row0"     : the FIRST row,    shape (5,)
#   "col0"     : the FIRST column, shape (4,)
#   "top_left" : the top-left 2x2 sub-matrix, shape (2, 2)
#   "every_other_row" : rows 0, 2, ..., shape (2, 5)
#
# Pattern to remember:
#   x[i]        -> i-th row
#   x[:, j]     -> j-th column
#   x[a:b, c:d] -> sub-matrix
#   x[::2, :]   -> every other row


def slice_demo(x):
    ...


x = np.arange(20).reshape(4, 5)
out = slice_demo(x)
assert np.array_equal(out["row0"], np.array([0, 1, 2, 3, 4]))
assert np.array_equal(out["col0"], np.array([0, 5, 10, 15]))
assert np.array_equal(out["top_left"], np.array([[0, 1], [5, 6]]))
assert np.array_equal(out["every_other_row"], np.array([[0, 1, 2, 3, 4], [10, 11, 12, 13, 14]]))
print("Task 3 passed")


# TASK 4 - Reshape and flatten
#
# Write reshape_demo(x): x is a flat array of length 12. Return a dict with:
#   "as_3x4"   : x reshaped to (3, 4)
#   "as_2x6"   : x reshaped to (2, 6)
#   "as_2x2x3" : x reshaped to (2, 2, 3)
#   "flat"     : x.flatten() (always 1-D)
#
# Pattern: x.reshape((a, b, c)) returns a VIEW (shares memory).
# x.flatten() returns a COPY. This matters when you start
# mutating tensors in-place.


def reshape_demo(x):
    ...


x = np.arange(12)
out = reshape_demo(x)
assert out["as_3x4"].shape == (3, 4)
assert out["as_2x6"].shape == (2, 6)
assert out["as_2x2x3"].shape == (2, 2, 3)
assert out["flat"].shape == (12,)
print("Task 4 passed")


# TASK 5 - Transpose
#
# Write transpose_demo(x): x is shape (2, 3). Return a dict with:
#   "T"          : x.T                       -> shape (3, 2)
#   "swap"       : x.transpose(1, 0)         -> same as T, shape (3, 2)
#   "perm_012"   : x.transpose(0, 1)         -> unchanged, shape (2, 3)
#
# Why it matters: attention scores in transformers need the last
# two dims swapped constantly. x.transpose(1, 0) is your friend.


def transpose_demo(x):
    ...


x = np.array([[1, 2, 3], [4, 5, 6]])
out = transpose_demo(x)
assert out["T"].shape == (3, 2)
assert out["swap"].shape == (3, 2)
assert out["perm_012"].shape == (2, 3)
print("Task 5 passed")


# TASK 6 - Matrix multiplication
#
# Write matmul_demo(A, B): A is (2, 3), B is (3, 4). Return a dict with:
#   "at_b"  : A @ B              -> shape (2, 4)
#   "dot"   : np.dot(A, B)       -> same shape, equivalent for 2-D
#   "BT"    : B.T                -> shape (4, 3)
#
# Key fact: (a, b) @ (b, c) -> (a, c). Inner dims must match.
# This is the single most important shape rule in all of ML.


def matmul_demo(A, B):
    ...


A = np.random.randn(2, 3)
B = np.random.randn(3, 4)
out = matmul_demo(A, B)
assert out["at_b"].shape == (2, 4)
assert out["dot"].shape == (2, 4)
assert out["BT"].shape == (4, 3)
print("Task 6 passed")


# TASK 7 - Elementwise operations
#
# Write elementwise(x): x is shape (3, 4). Return a dict with:
#   "scaled"    : x * 2.5
#   "shifted"   : x + 10
#   "neg"       : -x
#   "squared"   : x ** 2
#
# Elementwise means the operation applies independently to every
# entry. No shape change. In PyTorch this is exactly how tensors work.


def elementwise(x):
    ...


x = np.array([[1.0, -2.0], [3.0, -4.0], [0.5, 2.5]])
out = elementwise(x)
assert np.array_equal(out["scaled"], x * 2.5)
assert np.array_equal(out["shifted"], x + 10)
assert np.array_equal(out["neg"], -x)
assert np.array_equal(out["squared"], x ** 2)
print("Task 7 passed")


# TASK 8 - Reductions
#
# Write reduce_demo(x): x is shape (3, 4). Return a dict with:
#   "sum_all"   : x.sum()                 -> scalar
#   "sum_axis0" : x.sum(axis=0)           -> shape (4,)
#   "mean_all"  : x.mean()                -> scalar
#   "max_all"   : x.max()                 -> scalar
#   "argmax"    : x.argmax()              -> index of the biggest flat entry
#
# axis=0 collapses the rows (result has one value per column).
# axis=1 collapses the columns (result has one value per row).


def reduce_demo(x):
    ...


x = np.array([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]])
out = reduce_demo(x)
assert out["sum_all"] == 78.0
assert np.array_equal(out["sum_axis0"], np.array([15.0, 18.0, 21.0, 24.0]))
assert out["mean_all"] == 6.5
assert out["max_all"] == 12.0
assert out["argmax"] == 11
print("Task 8 passed")


# TASK 9 - Broadcasting
#
# Write broadcast_demo(x): x is shape (3, 4). Return a dict with:
#   "row_add"   : x + np.array([10, 20, 30, 40])    -> (3, 4)
#   "col_add"   : x + np.array([[1], [2], [3]])      -> (3, 4)
#   "scale"     : x * np.array([0.5])                -> (3, 4)
#
# Broadcasting rule (one sentence):
#   Shapes align from the RIGHT. Dimensions match if equal or one of them is 1.
# The smaller array gets "stretched" (logically, no copy) to the larger shape.
#
# Example: (3, 4) + (4,) -> (4,) is treated as (1, 4), stretched to (3, 4).


def broadcast_demo(x):
    ...


x = np.array([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]])
out = broadcast_demo(x)
assert np.array_equal(out["row_add"], x + np.array([10, 20, 30, 40]))
assert np.array_equal(out["col_add"], x + np.array([[1], [2], [3]]))
assert np.array_equal(out["scale"], x * np.array([0.5]))
print("Task 9 passed")


# TASK 10 - Softmax by hand
#
# Write softmax(x): x is a 1-D numpy array of logits (any real numbers).
# Return a 1-D array of the same shape where:
#   - entries are non-negative
#   - entries sum to 1.0
#   - the LARGEST logit becomes the LARGEST probability
#
# Recipe:
#   1. subtract max(x) for numerical stability (so exp doesn't blow up)
#   2. elementwise np.exp
#   3. divide by sum
#
# You will implement this AGAIN inside attention. Memorize it.


def softmax(x):
    ...


probs = softmax(np.array([1.0, 2.0, 3.0]))
assert probs.shape == (3,)
assert np.isclose(probs.sum(), 1.0)
assert probs[2] > probs[1] > probs[0]
assert np.isclose(probs[2], np.exp(1) / (np.exp(0) + np.exp(1) + np.exp(0)))
print("Task 10 passed")


# TASK 11 - Batch softmax (axis matters!)
#
# Write softmax_rows(X): X is shape (batch, features). Apply softmax
# INDEPENDENTLY to each row so every row sums to 1.0.
#
# Why it matters: in attention, softmax is applied along the LAST
# axis of a (batch, seq, seq) tensor. You need to be able to control
# WHICH axis gets normalized.


def softmax_rows(X):
    ...


X = np.array([[1.0, 2.0, 3.0], [10.0, 0.0, 0.0]])
out = softmax_rows(X)
assert out.shape == (2, 3)
assert np.allclose(out.sum(axis=1), np.array([1.0, 1.0]))
assert out[1, 0] > 0.99
print("Task 11 passed")