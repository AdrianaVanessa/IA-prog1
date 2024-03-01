#Práctica 1. Inteligencia Artificial
#Sánchez Barragán Rodrigo
#Trejo Reyes Adriana Vanessa
"""
Objetivo. Implementar dos agentes inteligentes. 

1.- El primer agente inteligente será el juego *adivina el número*: se deberá adivinar el número que está pensando el usuario , el usuario indicará si el número del agente es demasiado alto, demasiado bajo o correcto USANDO LA BÚSQUEDA BINARIA. El agente AJUSTA SU RANGO DE BÚSQUEDA EN FUNCIÓN DE LAS RESPUESTAS DEL USUARIO para acercarse al número correcto. PRIMERO PEDIR EL RANGO.

2.- El segundo agente inteligente será el juego *gato*, se debe implementar la lógica del juego y un agente que pueda jugar contra un usuario

"""
import sys #librería para salir del programa
import random # Se importa la libreria para dar moviento sin conciencia al jugador maquina

#++++++++++++++++++++++++++++++++++++++ adivina el número*********************************
def juego_adivina_numero():
    print("\nInstrucciones: Piense en un número aleatorio y nuestro agente inteligente lo adivinará\n¿En qué rango se encuentra el número? Ejemplo: Entre 1 y 10")
    inferior = int(input("\nIngrese el primer número del rango: ")) #obtenemos el limite inferior del rango
    superior = int(input("\nIngrese el último número del rango: ")) #obtenemos el limite superior rango
    lista_numeros = list(range(inferior, superior+1)) #creamos la lista con los números que se encuentran en el rango dado por el usuario, usamos la función range para eso

    busqueda_binaria(lista_numeros) #llamamos a la función para empezar con el alg busqueda binaria


#++++++++++++++++++++++++++++++++++++++ búsqueda binaria**************************************
def busqueda_binaria(lista_numeros):
    print(lista_numeros)
    punto_medio = len(lista_numeros)//2 #encontramos el punto medio de la lista de números que dio el usuario
    print(f"\n¿El número que tiene en mente es: {lista_numeros[punto_medio]} ?\nSi = 1\nEs menor = 2\nEs mayor = 3  ")
    respuesta= input()
    while True:
        if respuesta == "1":
            print(f"\nTu número adivinado es: {lista_numeros[punto_medio]}") #se adivinó el número
            break
        elif respuesta == "2":
            lista_numeros = lista_numeros[:punto_medio]  # ajustamos la lista para buscar en la mitad inferior usando :punto_medio, de esta manera realizamos una operación de segmentación de listas, se selecciona una subsecuencia de la lista lista_numeros desde el índice 0 hasta el elemento punto_medio sin incluirlo, asi se reduce la búsqueda a la mitad inferior de la lista y se AJUSTA EL RANGO DE BÚSQUEDA
            busqueda_binaria(lista_numeros)
        elif respuesta == "3":
            lista_numeros = lista_numeros[punto_medio + 1:]  # ajustamos la lista para buscar en la mitad superior usando punto_medio + 1:, de esta manera realizamos una operación de segmentación de listas se selecciona una subsecuencia de la lista lista_numeros desde el índice punto:medio hasta el último elemento de la lista sin incluirlo (punto:medio), asi se reduce la búsqueda a la mitad superior de la lista y se AJUSTA EL RANGO DE BÚSQUEDA
            busqueda_binaria(lista_numeros)
        else:
            print("\nRespuesta inválida. Por favor, elija 1, 2, o 3")
            respuesta= input()
    

#++++++++++++++++++++++++++++++++++++++ gato **************************************
# En esta funcion se manda una lista de listas conteniendo los elementos previamente
# registrados, ya sean vacios por el inicio del juego o los regsitrados por la maquina o jugador
def imprimirTablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

# Aqui es donde va a recorrer cada parte del juego para verificar si ya hubo un ganador considerando fila,
# Columna u diagonales
def veriGanador(tablero):
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != ' ':
            return True

    # Verificar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != ' ':
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != ' ':
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != ' ':
        return True

    return False

# En esta funcion buscara lugares vacios dentro de la lista de listas y de ello obtendra un lugar aleatorio
def movMaquina(tablero):
    casillasLibre = [(fila, columna) for fila in range(3) for columna in range(3) if tablero[fila][columna] == ' ']
    return random.choice(casillasLibre)



def jugarGato():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        print("\nInstrucciones. Seleccione la casilla en la que quiere poner su movimiento con el formato: (fila,columna), ejemplo: 1,1\nLas filas son 0,1 y 2, las columnas son 0,1 y 2\n")
        imprimirTablero(tablero)

        # Turno del jugador
        movJugador = input("\nEs tu turno jugador X:\n")
        fila, columna = map(int, movJugador.split(','))

        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = 'X'
            if veriGanador(tablero):
                imprimirTablero(tablero)
                print("¡Jugador X gana!")
                break
        else:
            print("Movimiento inválido. La casilla ya está ocupada.")

        # Turno de la maquina
        maquinaFila, maquinaColumna = movMaquina(tablero)
        tablero[maquinaFila][maquinaColumna] = 'O'
        if veriGanador(tablero):
            imprimirTablero(tablero)
            print("¡Jugador O gana!")
            break

        if ' ' not in [casilla for fila in tablero for casilla in fila]:
            imprimirTablero(tablero)
            print("El juego ha terminado en empate.")
            break

#++++++++++++++++++++++++++++++++++++++ Menú principal de la aplicación+++++++++++++++++++++++++++++++++++++++++
while True:
    print("\n\nBienvenido. Seleccione una opción para jugar con un agente inteligente.")
    print("1. Juego: Adivina el número")
    print("2. Juego: Gato (Tic-Tac-Toe)")
    print("3. Salir")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        juego_adivina_numero() #se llama a la funcion definida para adivina el número
    elif opcion == "2":
        jugarGato() #se llama a la funcion definida para gato
    elif opcion == "3":
        print("\n¡Vuelva pronto!\n")
        sys.exit() #sale del programa
    else:
        print("Opción inválida. Intente nuevamente.")