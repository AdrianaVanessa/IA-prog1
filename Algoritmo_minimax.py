#Algoritmo minimax
#Trejo Reyes Adriana Vamessa

#se define la clase del juego gato
class gato:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    # se cambia el estado juego al estado dado
    def configurar_estado(self, nodo_ini):
        self.board = nodo_ini

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_winner(self, player):
        # Comprobar filas
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Comprobar columnas
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        # Comprobar diagonales
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_full()

    def get_empty_cells(self):
        return [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == ' ']

    def make_move(self, player, row, col):
        self.board[row][col] = player

    def undo_move(self, row, col):
        self.board[row][col] = ' '


def minimax(board, maximizing_player):
    if board.is_winner('X'):
        return 1
    elif board.is_winner('O'):
        return -1
    elif board.is_full():
        return 0

    if maximizing_player:
        best_score = float('-inf')
        for row, col in board.get_empty_cells():
            board.make_move('X', row, col)
            score = minimax(board, False)
            board.undo_move(row, col)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row, col in board.get_empty_cells():
            board.make_move('O', row, col)
            score = minimax(board, True)
            board.undo_move(row, col)
            best_score = min(score, best_score)
        return best_score


def find_best_move(board):
    best_score = float('-inf')
    best_move = None
    for row, col in board.get_empty_cells():
        board.make_move('X', row, col)
        score = minimax(board, False)
        board.undo_move(row, col)
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move


#+++++++++++++++++++++++++++++++ menú principal de la aplicación +++++++++++++++++++++++++++++++
# se crea una instancia de la clase gato y asigna a "juego"
juego = gato()

"mediante una lista de listas, creamos el nodo inicial de la partida, en donde la computadora será el jugador MAX -> X y el usuario será el jugador MIN -> O"
nodo_inicial = [
        ['X', 'O', 'O'],
        ['X', ' ', ' '],
        ['O', 'X', ' ']
    ]

# se utiliza el método para asignar el estado del nodo_inicial al tablero del juego juego
juego.configurar_estado(nodo_inicial)

# se  imprime el tablero
juego.print_board()


# iniciale el buble principal hasta que alguien gane o sea empate
while not juego.game_over():
    computer_row, computer_col = find_best_move(juego)
    print(f"La computadora juega en la fila {computer_row} y columna {computer_col}")
    juego.make_move('X', computer_row, computer_col)
    juego.print_board()

    if juego.game_over():
        break

    player_row, player_col = map(int, input("Ingrese su movimiento (fila columna): ").split())
    juego.make_move('O', player_row, player_col)
    juego.print_board()

if juego.is_winner('X'):
    print("Gana jugador MAX")
elif juego.is_winner('O'):
    print("Gana jugador MIN")
else:
    print("Empate")

