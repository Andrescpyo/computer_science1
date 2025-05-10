
from fix_notation import FixNotation as fn
from tree_visual import ExpressionTreeVisualizer as etv

infix = "2 + (1/2) - (3/2)^2"
postfix = fn.to_postfix(infix)
prefix = fn.to_prefix(infix)

print(postfix)
print(prefix)

tree = etv.build_tree_from_postfix(postfix)
etv.generate_image(tree, "postfix_tree")
