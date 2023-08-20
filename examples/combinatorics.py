# Combinatorics
from itertools import permutations, combinations
import torch
from pprint import pprint

elements = torch.Tensor([1, 2, 3])
perm = list(permutations(elements))
comb = list(combinations(elements, 2))

print("Permutations:")
pprint(perm)
print("Combinations:")
pprint(comb)