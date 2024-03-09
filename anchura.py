
import os

#Representamos el grafo o arbol en forma de diccionario

grafo = {'60': ['41','74'],
         '41': ['60','16','53'],
         '74': ['60','65'],
         '16': ['41','25'],
         '53': ['41','46','55'],
         '65': ['74','63','70'],
         '25': ['16'],
         '46': ['53','42'],
         '55': ['53'],
         '63': ['65','62','64'],
         '70': ['65'],
         '42': ['46'],
         '62': ['63'],
         '64': ['63']}

#Numero que se va a buscar
num_a_buscar = '42'

#lista auxiliar para definir que nodos ya visitammos
visitados = []
#Definimos una lista que servira de cola para esta busqueda
cola = []
print("Busqueda en anchura")
#Definicion del nodo raiz(o por cual que empezara a buscar)
origen = input("Que nodo es raiz? ")
print("\nLista de busqueda por anchura\n")

#metemos en la cola el primer nodo raiz
cola.append(origen)

#mientras la cola no este vacia
while cola:
    #desencolamos el primer elemento de nuestra cola
    actual = cola.pop(0)

    if actual not in visitados:
        print(" ", actual)
        visitados.append(actual)

    if actual == num_a_buscar:
        print("\nNumero encontrado")
        exit()
    
    #por cada vertice conexo al vertice actual que no ha sido visitado
    #encolar vertice(s)
    for key in grafo[actual]:
        if key not in visitados:
            cola.append(key)

print("\nEl numero ", num_a_buscar)
print(" no exite en el grafo.")
