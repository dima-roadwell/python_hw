# Задача XO необязательная.
# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
import random

class Game:
    _game_field = []
    _is_game_over = False

    def __init__(self, rows, cols, player_sign):
        self.player_sign = player_sign.upper()
        self.rows = rows
        self.cols = cols
        self.turns_count = self.rows * self.cols

        if self.player_sign == "X":
            self.bot_sign = "O"
        else:
            self.bot_sign = "X"
        
        self.create_field()
    
    def create_field(self):
        for i in range(self.rows):
            self._game_field.append([" "] * self.cols)
    
    def set_user_turn(self):
        turn = input("Input your turn (example: '1 1'): ")
        turn = turn.split()

        if self.check_empty_cell(turn):
            self.change_turns_count()
        else:
            print("This cell isn't empty!") 
            self.set_user_turn()

        return turn
    
    def set_bot_turn(self):
        available_turns = []

        for i in range(len(self._game_field)):
            for j in range(len(self._game_field[i])):
                if self._game_field[i][j] == " ":
                    available_turns.append([i, j])

        rnd = random.randint(0, len(available_turns) - 1)
        turn = available_turns[rnd]

        for i in range(len(turn)):
            turn[i] += 1

        self.change_turns_count()

        return turn
    
    def check_empty_cell(self, turn) -> bool:
        if  self._game_field[int(turn[0]) - 1][int(turn[1]) - 1] == " ":
            return True
        else:
            return False

    def change_turns_count(self):
        self.turns_count -= 1
    
    def change_field(self, turn, sign):
        self._game_field[int(turn[0]) - 1][int(turn[1]) - 1] = sign

    def check_game_over(self):
        if self.turns_count == 0:
            self._is_game_over = True

    def check_win(self):
        line_win = [0, 1, 2]
        is_win = False

        for i in range(self.rows):
            if self._game_field[line_win[0]][i] != " " and self._game_field[line_win[0]][i] == self._game_field[line_win[1]][i] and self._game_field[line_win[0]][i] == self._game_field[line_win[2]][i]:
                is_win = True
                break
            elif self._game_field[i][line_win[0]] != " " and self._game_field[i][line_win[0]] == self._game_field[i][line_win[1]] and self._game_field[i][line_win[0]] == self._game_field[i][line_win[2]]:
                is_win = True
                break
            elif self._game_field[line_win[0]][line_win[0]] != " " and self._game_field[line_win[0]][line_win[0]] == self._game_field[line_win[1]][line_win[1]] and self._game_field[line_win[0]][line_win[0]] == self._game_field[line_win[2]][line_win[2]]:
                is_win = True
                break
            elif self._game_field[line_win[0]][line_win[2]] != " " and self._game_field[line_win[0]][line_win[2]] == self._game_field[line_win[1]][line_win[1]] and self._game_field[line_win[0]][line_win[2]] == self._game_field[line_win[2]][line_win[0]]:
                is_win = True
                break

        return is_win


    def display_field(self):
        for i in range(len(self._game_field)):
            print()
            for j in range(len(self._game_field[i])):
                print(self._game_field[i][j], end=" | ")
        print()

player_sign = input("Choose your sign (X or O)): ")
game = Game(3, 3, player_sign)
game.display_field()

while not game._is_game_over:
    game.change_field(game.set_user_turn(), game.player_sign)
    game.display_field()
    game.change_field(game.set_bot_turn(), game.bot_sign)
    game.display_field()

    if game.check_win():
        print("Game is over!")
        break

    game.check_game_over()