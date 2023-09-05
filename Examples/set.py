def demonstrate_set_theory():
    A = {1, 2, 3}
    B = {3, 4, 5}
    union_set = A.union(B)
    intersection_set = A.intersection(B)
    difference_set = A.difference(B)
    
    print("Set Theory:")
    print("Union:", union_set)
    print("Intersection:", intersection_set)
    print("Difference:", difference_set)

# Run the demonstration
if __name__ == "__main__":
    demonstrate_set_theory()
