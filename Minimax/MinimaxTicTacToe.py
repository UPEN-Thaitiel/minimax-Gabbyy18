
import math

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.human = "H"
        self.ai = "I"
        self.current_player = self.human

    def print_board(self):
        print("\nTABLERO")
        for i in range(3):
            row = self.board[i*3:(i+1)*3]
            print(" " + " | ".join(row))
            if i < 2:
                print("---|---|---")
        print()

    def is_full(self):
        return " " not in self.board

    def check_winner(self):
        combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return None

    def make_move(self, index, player):
        if 0 <= index <= 8 and self.board[index] == " ":
            self.board[index] = player
            return True
        return False

    def minimax(self, is_maximizing):
        winner = self.check_winner()
        if winner == self.ai:
            return 1
        elif winner == self.human:
            return -1
        elif self.is_full():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = self.ai
                    score = self.minimax(False)
                    self.board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = self.human
                    score = self.minimax(True)
                    self.board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -math.inf
        move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.ai
                score = self.minimax(False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    move = i
        if move is not None:
            self.make_move(move, self.ai)
            print(f"\nLa IA juega en: {move + 1}")

    def play(self):
        print("Bienvenido a Tic Tac Toe - Tú (H) vs IA (I)")
        self.print_board()
        while True:
            if self.current_player == self.human:
                try:
                    move = int(input("Selecciona una casilla (1-9): ")) - 1
                    if self.make_move(move, self.human):
                        self.current_player = self.ai
                    else:
                        print("Posición inválida.")
                        continue
                except ValueError:
                    print("Entrada no válida. Usa un número del 1 al 9.")
                    continue
            else:
                self.best_move()
                self.current_player = self.human

            self.print_board()
            winner = self.check_winner()
            if winner:
                print(f"¡Ganador: {winner}!")
                break
            elif self.is_full():
                print("Empate.")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
