
from fix_notation import FixNotation as fn
from tree_visual import ExpressionTreeVisualizer

infix = "35+7*3-105/(7*5)"
postfix = fn.to_postfix(infix)
prefix = fn.to_prefix(infix)

print(postfix)
print(prefix)

tree = ExpressionTreeVisualizer.build_tree_from_postfix(postfix)
ExpressionTreeVisualizer.generate_image(tree, "my_tree")
