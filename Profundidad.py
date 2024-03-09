"""Definición de la clase nodo que define la estructura de un nodo individual en el árbol"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""Definición de la funcion de busqueda en profundidad"""

def profundidad(raiz, busqueda):
    if raiz is None:
        return False
    
    print(f"{raiz.value} ", end="")

    if raiz.value == busqueda:
        return True
    
    if raiz.left != None:
        res = profundidad(raiz.left, busqueda)
        if res == True:
            return True
    
    if raiz.right != None:
        res = profundidad(raiz.right, busqueda)
        if res == True:
            return True
    
    return

"""Construcción del árbol"""

arbol = Node(60)
arbol.left = Node(41)
arbol.right = Node(74)
arbol.left.left = Node(16)
arbol.left.right = Node(53)
arbol.left.left.right = Node(25)
arbol.left.right.left = Node(46)
arbol.left.right.left.left = Node(42)
arbol.left.right.right = Node(55)
arbol.right.left = Node(65)
arbol.right.left.left = Node(63)
arbol.right.left.right = Node(70)
arbol.right.left.left.left = Node(62)
arbol.right.left.left.right = Node(64)

"""Variable que almacena el valor que se desea encontrar en el árbol"""

valor_a_buscar = 42

"""Llamada a la función de busqueda"""

busqueda = profundidad(arbol, valor_a_buscar)

if busqueda:
    print(f"\nEl valor {valor_a_buscar} se encuentra en el árbol")
else:
    print(f"\nEl valor {valor_a_buscar} no se encuentra en el árbol")