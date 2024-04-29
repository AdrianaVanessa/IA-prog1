# Representación del tablero de gato
tablero =  [[' ' for _ in range(3)] for _ in range(3)]

# Jugadores
jugadorHumano = 'O'
jugadorIA = 'X'

# Función para imprimir el tablero en la consola
def imprimirTablero(tablero):
    for fila in tablero:
        print('|'.join(fila))
        print('-----')

# Función para verificar si hay un ganador o empate
def verificarGanador(tablero):
    # Revisa filas
    for fila in tablero:
        if fila.count(fila[0]) == len(fila) and fila[0] != ' ':
            return fila[0]

    # Revisa columnas
    for col in range(len(tablero[0])):
        if all(tablero[fila][col] == tablero[0][col] and tablero[fila][col] != ' ' for fila in range(len(tablero))):
            return tablero[0][col]

    # Revisa diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ' or tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[1][1]

    # Revisa si hay empate
    if all(tablero[fila][col] != ' ' for fila in range(len(tablero)) for col in range(len(tablero[0]))):
        return 'empate'

    return None

# Función para evaluar el tablero y devolver la puntuación
def evaluarTablero(tablero):
    ganador = verificarGanador(tablero)
    if ganador == jugadorIA:
        return 10
    elif ganador == jugadorHumano:
        return -10
    else:
        return 0

# Función para implementar el algoritmo minimax
def minimax(tablero, profundidad, maximizando):
    puntuacion = evaluarTablero(tablero)

    # Caso base: si el juego ha terminado o se alcanza la profundidad máxima
    if puntuacion == 10 or puntuacion == -10 or verificarGanador(tablero) == 'empate':
        return puntuacion

    if maximizando:
        mejorPuntuacion = -float('inf')
        for fila in range(len(tablero)):
            for col in range(len(tablero[0])):
                if tablero[fila][col] == ' ':
                    tablero[fila][col] = jugadorIA
                    mejorPuntuacion = max(mejorPuntuacion, minimax(tablero, profundidad + 1, False))
                    tablero[fila][col] = ' '
        return mejorPuntuacion
    else:
        mejorPuntuacion = float('inf')
        for fila in range(len(tablero)):
            for col in range(len(tablero[0])):
                if tablero[fila][col] == ' ':
                    tablero[fila][col] = jugadorHumano
                    mejorPuntuacion = min(mejorPuntuacion, minimax(tablero, profundidad + 1, True))
                    tablero[fila][col] = ' '
        return mejorPuntuacion

# Función para encontrar el mejor movimiento para la computadora
def encontrarMejorMovimiento(tablero):
    mejorPuntuacion = -float('inf')
    mejorMovimiento = None
    for fila in range(len(tablero)):
        for col in range(len(tablero[0])):
            if tablero[fila][col] == ' ':
                tablero[fila][col] = jugadorIA
                puntuacion = minimax(tablero, 0, False)
                tablero[fila][col] = ' '
                if puntuacion > mejorPuntuacion:
                    mejorPuntuacion = puntuacion
                    mejorMovimiento = (fila, col)
    return mejorMovimiento

# Función para el turno del jugador humano
def turnoJugadorHumano(tablero):
    while True:
        movJugador = input("Jugador X, elige tu movimiento (fila,columna): ")
        fila, col = map(int, movJugador.split(','))
        if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == ' ':
            tablero[fila][col] = jugadorHumano
            break
        else:
            print("Movimiento inválido. Intente de nuevo.")

# Función principal para ejecutar el juego
def jugarGato():
    jugadorActual = jugadorHumano
    while True:
        imprimirTablero(tablero)
        if jugadorActual == jugadorHumano:
            turnoJugadorHumano(tablero)
        else:
            movimiento = encontrarMejorMovimiento(tablero)
            tablero[movimiento[0]][movimiento[1]] = jugadorIA
            print(f"La IA ha hecho su movimiento en la fila {movimiento[0]} y columna {movimiento[1]}")
        ganador = verificarGanador(tablero)
        if ganador:
            imprimirTablero(tablero)
            if ganador == 'empate':
                print("¡Empate!")
            elif ganador == jugadorIA:
                print("¡La IA ha ganado!")
            else:
                print("¡Has ganado!")
            break
        jugadorActual = jugadorHumano if jugadorActual == jugadorIA else jugadorIA

# Iniciar el juego
jugarGato()
