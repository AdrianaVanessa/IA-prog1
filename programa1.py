#Programa 1. Inteligencia Artificial
#Manejo de cadenas, listas, tuplas y diccionarios
#Sánchez Barragán Rodrigo
#Trejo Reyes Adriana Vanessa


#----------------------------- cadenas o strings------------------------------
cadena = "Hola, mundo!"
print(cadena[0])        
print(cadena[0:4])      # 0 a 3
print(len(cadena))      
print(cadena + "como estas")  

#----------------------------- listas------------------------------
lista = [1, 2, 3, 4, 5]
print(lista[0])         
print(lista[2:4])       # 2 a 3
lista.append(6)         # concatena al final
print(lista)
lista.extend([7, 8])    # agrega al final de la lista otra lista
lista.remove(3)         # eliminar
print(lista)

#----------------------------- tuplas------------------------------
valor1=23
tupla = (1, 2, 3, 4, 5, 'hola', 'jejeje deojwdo', valor1)
print(tupla[0])        
print(tupla[2:4])       # 2 a 3
print(len(tupla))       


#----------------------------- diccionario------------------------------
mes = "Enero"

if(mes == "Enero"):
    print(1)
elif(mes == "Febrero"):
    print(2)


diccionario = {
    "Enero":1, #la llave es Enero
    "Febrero":2,
    "Marzo":3,
    "Pablo":1234
}

print(diccionario["Enero"])
print(diccionario["Pablo"])
#################################################################################################