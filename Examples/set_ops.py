# Ethan Bleier
# 8/29/23
# ChatGPt "discrete math set operation python examples"
# Using built-in python functions for the operations.
# Check out /UnionAndIntersection/ to see the behind the scenes of these ops

# Define two sets
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

# Union of two sets
union_result = set_A.union(set_B)
print("Union:", union_result)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of two sets
intersection_result = set_A.intersection(set_B)
print("Intersection:", intersection_result)  # Output: {4, 5}

# Difference between two sets
difference_result = set_A.difference(set_B)
print("Difference (A - B):", difference_result)  # Output: {1, 2, 3}

# Symmetric Difference between two sets
symmetric_difference_result = set_A.symmetric_difference(set_B)
print("Symmetric Difference:", symmetric_difference_result)  # Output: {1, 2, 3, 6, 7, 8}

# Check if a set is a subset of another set
is_subset = set_A.issubset(set_B)
print("Is A a subset of B?", is_subset)  # Output: False

# Check if a set is a superset of another set
is_superset = set_A.issuperset(set_B)
print("Is A a superset of B?", is_superset)  # Output: False

# Add an element to a set
set_A.add(6)
print("Updated set A:", set_A)  # Output: {1, 2, 3, 4, 5, 6}

# Remove an element from a set
set_B.remove(6)
print("Updated set B:", set_B)  # Output: {4, 5, 7, 8}
