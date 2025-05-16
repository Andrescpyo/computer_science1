
from tree import BinaryTree
from tree_visual import BinaryTreeVisualizer as btv

tree = BinaryTree()
tree.insert(12)
tree.insert(17)
tree.insert(25)
tree.insert(10)
tree.insert(15)
tree.insert(17)
tree.insert_list([8, 6, 4, 1, 2])
tree.insert_list([20, 19, 40, 52, 60, 70, 69])

print(tree.search(8))

print("\nInorder traversal:")
print(tree.inorder_traversal(tree.root))

btv.plot(tree, "tree.png")
