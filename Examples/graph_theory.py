import networkx as nx

G = nx.Graph() 
tree = [1, [2, [4], [5]], [3]]

relations = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['David'],
    'Charlie': ['Eve']
}
print("Discrete Structures:")
print("Tree:", tree)
print("Relations:", relations)
print()

# === Notes ===
'''

tree = [1, [2, [4], [5]], [3]]
Looks like: 

       1
     /   \
    2     3
   / \
  4   5

In many cases, the first element in a nested list within a
tree-like structure is used to represent the root node. 
However, it's not a strict rule that the first element must always 
represent the root node. The structure and interpretation 
of the nested list depend on the context and how the data is organized.

For example, in the nested list tree = [1, [2, [4], [5]], [3]], the first element 
1 is indeed used to represent the root node of the tree. But depending on the 
application and how the nested list is used, the first element might not always 
represent the root node. It's important to document and communicate the structure 
of your data to ensure proper understanding and interpretation.

Output: 
Relations: {'Alice': ['Bob', 'Charlie'], 'Bob': ['David'], 
'Charlie': ['Eve']}


'''