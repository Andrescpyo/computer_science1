from tree import BinaryTree
from tree_visual import BinaryTreeVisualizer as btv

tree = BinaryTree()
tree.insert_list([700, 20, 1042, 1024, 64, 12, 3, 19, 546, 223, 1, 1000, 365, 6, 2025, 815, 2023,815])
tree2 = BinaryTree()
tree2.insert_list([724, 699, 698, 697, 696, 695, 694, 693, 692, 691, 690, 689, 688, 687, 686, 681, 682])

print("\n--- Caracteristicas del árbol 1 ---")
print(f"En el arbol 1 hay algun nodo con valor 8?:  {tree.search(8)}") #print if node with value 8 exists
print(f"En el arbol 1 hay algun nodo con valor 12?:  {tree.search(12)}")
print(f"El arbol 1 es de grado {tree.grade} y") #print tree grade
print(f"Tiene {tree.height} de altura") #print tree height
print(f"Si el arbol 1 estuviera balanceado su altura seria: {tree.balanced_height:.2f}") #print balanced tree height
print(f"El arbol 1 tiene {tree.nodes} nodos\n") #print tree nodes

print("\n--- Caracteristicas del árbol 2 ---")
print(f"El arbol 2 cuenta con {tree2.nodes} nodos y") #print tree2 nodes
print(f"Tiene {tree2.height} de altura") #print tree2 height
print(f"El arbol 2 es de grado {tree2.grade}") #print tree2 grade
print(f"Si el arbol 2 estuviera balanceado su altura seria: {tree2.balanced_height:.2f}") #print balanced tree2 height

print("\nInorder traversal del arbol 1:")
print(tree)
print("\nInorder traversal del arbol 2:")
print(tree2)

print("\n--- Propiedades del Arbol 1 ---")
print(f"¿Es el Arbol 1 un arbol lleno? {tree.is_full()}")
print(f"¿Es el Arbol 1 un arbol completo? {tree.is_complete()}")
print(f"¿Es el Arbol 1 un arbol perfecto? {tree.is_perfect()}")

print("\n--- Propiedades del Arbol 2 ---")
print(f"¿Es el Arbol 2 un arbol lleno? {tree2.is_full()}")
print(f"¿Es el Arbol 2 un arbol completo? {tree2.is_complete()}")
print(f"¿Es el Arbol 2 un arbol perfecto? {tree2.is_perfect()}")

btv.plot(tree, "tree.png")
btv.plot(tree2, "tree2.png")

tree.delete(12)
tree.delete(1024)
print("\nInorder traversal del arbol 1 despues de eliminar nodos:")
print(f"{tree}")
btv.plot(tree, "new_tree.png")

tree2.insert(812)
tree2.insert(1024)
print("\nInorder traversal del arbol 1 despues de agregar nodos:")
print(f"{tree2}\n")
btv.plot(tree2, "new_tree2.png")

#New prints for tree properties.
tree3 = BinaryTree()
tree3.insert_list([50, 25, 75, 10, 30, 60, 80]) #An initially full and complete tree (height 3)

btv.plot(tree3, "tree3_perfecto.png")
print(f"Arbol 3 inicial (Inorder): {tree3}")
print(f"Altura: {tree3.height}, Nodos: {tree3.nodes}")
print(f"¿Es lleno? {tree3.is_full()}") # true
print(f"¿Es completo? {tree3.is_complete()}") # true
print(f"¿Es perfecto? {tree3.is_perfect()}\n") # true

tree3.delete(10)
tree3.delete(30)
btv.plot(tree3, "tree3_lleno.png")
print(f"Arbol 3 (Inorder) despues de eliminar 10: {tree3}")
print(f"Altura: {tree3.height}, Nodos: {tree3.nodes}")
print(f"¿Es lleno? {tree3.is_full()}") # true
print(f"¿Es completo? {tree3.is_complete()}") # false
print(f"¿Es perfecto? {tree3.is_perfect()}\n") # false

tree3.insert(5)
tree3.insert(27)
tree3.delete(80)
btv.plot(tree3, "tree3_completo.png")
print(f"Arbol 3 (Inorder) despues de agregar 5: {tree3}")
print(f"Altura: {tree3.height}, Nodos: {tree3.nodes}")
print(f"¿Es lleno? {tree3.is_full()}") # false
print(f"¿Es completo? {tree3.is_complete()}") # true
print(f"¿Es perfecto? {tree3.is_perfect()}\n") # false