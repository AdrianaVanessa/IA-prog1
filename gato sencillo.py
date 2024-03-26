
# Se importa la libreria para dar moviento sin conciencia al jugador maquina
import random

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

# En esta funcion se creara la lista de listas de los movimientos registrado e iniciara un bucle
# para ir alternando entre jugador y maquina
def jugarGato():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        imprimirTablero(tablero)

        # Turno del jugador
        movJugador = input("Jugador X, elige tu movimiento (fila,columna): ")
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

# En esta funcion del "main" es donde inicia todo el juego
jugarGato()
