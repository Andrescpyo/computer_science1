
from tree import BinaryTree
from tree_visual import BinaryTreeVisualizer as btv

tree = BinaryTree()
tree.insert_list([700, 20, 1042, 1024, 64, 12, 3, 19, 546, 223, 1, 1000, 365, 6, 2025, 815, 2023,815])
tree2 = BinaryTree()
tree2.insert_list([700, 699, 698, 697, 696, 695, 694, 693, 692, 691, 690, 689, 688, 687, 686, 681, 682,700])

print(tree.search(8))
print(tree.grade)
print(f"Altura del arbol 1: {tree.height}")
print(f"Altura balanceada del arbol 1: {tree.balanced_height:.2f}")
print(f"Nodos del arbol 1: {tree.nodes}")

print(f"Altura del arbol 2: {tree2.height}")

print("\nInorder traversal:")
print(tree)


btv.plot(tree, "tree.png")
btv.plot(tree2, "tree2.png")

tree.delete(12)
print("\nInorder traversal:")
print(tree)
btv.plot(tree, "new_tree.png")
