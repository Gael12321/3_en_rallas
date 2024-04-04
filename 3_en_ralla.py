from typing import Tuple, Iterable

State = [[" " for _ in range(3)] for _ in range(3)]
Action = Tuple[int, int]
Player = Tuple[str, str] 
Utility = float

class TicTacToe(Game):
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def initial(self) -> State:
        return [[" " for _ in range(3)] for _ in range(3)]
    
    def player(self, s: State) -> Player:
        return "X" if sum(row.count("X") for row in s) == sum(row.count("O") for row in s) else "O"
    
    def actions(self, s:State) -> Iterable[Action]:
        return [(i, j) for i in range(3) for j in range(3) if s[i][j] == " "]
    
    def result(self, s: State, a: Action) -> State:
        i, j = a
        s[i][j] = self.player(s)
        return s
    
    def final(self, s: State) -> bool:
        for i in range(3):
            if all(cell == "X" for cell in s[i]) or all(cell == "O" for cell in s[i]):
                return True
            if all(s[j][i] == "X" for j in range(3)) or all(s[j][i] == "O" for j in range(3)):
                return True
        if all(s[i][i] == "X" for i in range(3)) or all(s[i][i] == "O" for i in range(3)):
            return True
        if all(s[i][2 - i] == "X" for i in range(3)) or all(s[i][2 - i] == "O" for i in range(3)):
            return True
        if all(cell != " " for row in s for cell in row):
            return True
        return False  

    def utility(self, s: State, p: Player) -> Utility:
        assert self.final(s)
        sp, sn = s
        if sp == p:
            return float("inf") * -1
        elif sp == " ":
            return 0
        else:
            return float("inf")


    def show(self, s: State) -> None:
        for row in s:
            print(" | ".join(row))
            print("-" * 5)
        print()





"""     def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def play_game(self, player1_fn, player2_fn):
        self.print_board()

        while True:
            if self.current_player == "X":
                action = player1_fn(self.board)
            else:
                action = player2_fn(self.board)

            if self.board[action[0]][action[1]] == " ":
                self.board[action[0]][action[1]] = self.current_player
                self.print_board()
                if self.check_win(self.current_player):
                    print(f"Jugador {self.current_player} Gana!")
                    break
                elif self.check_draw():
                    print("GG Empate")
                    break
                self.current_player = "O" if self.current_player == "X" else "X"
            else:
                print("Papeada")

def human_player(board):
    while True:
        try:
            row = int(input("Fila (0-4): "))
            col = int(input("Columna (0-4): "))
            if 0 <= row <= 4 and 0 <= col <= 4:
                return row, col
            else:
                print("Todo wey")
        except ValueError:
            print("Xd")

def random_player(board):
    available_moves = [(i, j) for i in range(5) for j in range(5) if board[i][j] == " "]
    return random.choice(available_moves)
 """
""" game = TicTacToe()
game.play_game(human_player, random_player) """



""" def random_number():
    Cara = "Aguila","Sol"
    return random.choice(Cara)

def CajaA(Cara):
    if Cara == "Aguila":
        return -50
    else:
        return 50

def CajaB(Cara):
    if Cara == "Aguila":
        return 1
    else:
        return 3
def CajaC(Cara):
    if Cara == "Aguila":
        return -5
    else:
        return 15



def loopA(n):
    total = 0
    for _ in range(n):
        Cara = random_number()
        total += CajaA(Cara)
    return total/n

def LoopB(n):
    total = 0
    for _ in range(n):
        Cara = random_number()
        total += CajaB(Cara)
    return total/n

def LoopC(n):
    total = 0
    for _ in range(n):
        Cara = random_number()
        total += CajaC(Cara)
    return total/n
 """