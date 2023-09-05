# Created by ChatGPT on 2023-09-05
# This code demonstrates a custom union method for "sets" in discrete math set theory
# please correct me: ebleier4@gmail.com

def custom_union(list1, list2):
    # Combine both lists and convert them to a set to remove duplicates
    union_set = set(list1 + list2)
    
    # Convert the set back to a list to maintain the order
    union_list = list(union_set)
    
    return union_list

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = custom_union(list1, list2)
print(result)
