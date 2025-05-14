
from tree import BinaryTree
from tree_visual import ExpressionTreeVisualizer as etv

tree = BinaryTree()
tree.insert(12)
tree.insert(17)
tree.insert(25)
tree.insert(10)
tree.insert(15)
tree.insert(17)
print(tree.search(8))

print("Inorder traversal:")
#tree.inorder_traversal(tree.root)

tree.delete(10)

print("\nInorder traversal:")
print(tree.inorder_traversal(tree.root, ""))

# vtree = etv.build_tree_from_postfix(tree.inorder_traversal(tree.root))
#etv.generate_image(tree, "tree")
