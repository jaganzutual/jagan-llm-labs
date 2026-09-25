import torch

# Step 1: word -> id.
# This dict is the only place that knows words.
# "i" gets id 1, "love" gets id 2, "cats" gets id 3.
word_dict = {
    "i": 1,
    "love": 2,
    "cats": 3
}

# Step 2: id -> vector holder.
# Embedding knows no words, only rows 0-9.
# Shape (10, 4) = 10 possible ids, 4 numbers per id.
# Rows start random, training will shape them.
emb = torch.nn.Embedding(10, 4)

# Step 3: sentence as ids.
# "i love cats" -> [1, 2, 3] via word_dict above.
# Outer [] = batch = 1 sentence together.
# Inner [1, 2, 3] = seq_len = 3 tokens.
# Shape (1, 3).
ids = torch.tensor([[1, 2, 3]])

# Step 4: lookup.
# id 1 pulls row 1, id 2 pulls row 2, id 3 pulls row 3.
# Output shape (1, 3, 4) = (batch, seq_len, dim).
out = emb(ids)
print(out)
print(out.shape)
