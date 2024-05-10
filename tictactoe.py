import random
import time


class Tictactoe:
    def __init__(self):
        self.player_x = Player()
        self.player_y = Player()
        self.won = False
        self.turn = True
        self.marks = ["x", "o"]
        self.rounds = 0

    def ask_names(self):
        print('Welcome to Tic Tac Toe')
        time.sleep(1.5)
        print('Player 1 Enter your name: ')
        self.player_x.name = input("--> ")
        time.sleep(0.5)
        print('Player 2 Enter your name: ')
        self.player_y.name = input("--> ")

    def choose_x_or_o(self):
        players = [self.player_x, self.player_y]
        random_player = players[random.randint(0, 1)]
        other_player = players[1] if players[0] == random_player else players[0]
        time.sleep(0.5)
        print(f'{random_player.name}, Choose a mark: x or o')
        mark = input("--> ")
        time.sleep(0.5)
        random_player.mark = mark
        other_player.mark = self.marks[1] if self.marks[0] == mark else self.marks[0]

        print(f'''
        {random_player.name}:{random_player.mark}
        {other_player.name}: {other_player.mark}
        ''')

    def check_turn(self):
        self.turn = not self.turn
        return self.turn

    def grid(self):
        one = self.player_x.mark if self.player_x.turns[0] else (self.player_y.mark if self.player_y.turns[0] else '')
        two = self.player_x.mark if self.player_x.turns[1] else (self.player_y.mark if self.player_y.turns[1] else '')
        three = self.player_x.mark if self.player_x.turns[2] else (self.player_y.mark if self.player_y.turns[2] else '')
        four = self.player_x.mark if self.player_x.turns[3] else (self.player_y.mark if self.player_y.turns[3] else '')
        five = self.player_x.mark if self.player_x.turns[4] else (self.player_y.mark if self.player_y.turns[4] else '')
        six = self.player_x.mark if self.player_x.turns[5] else (self.player_y.mark if self.player_y.turns[5] else '')
        seven = self.player_x.mark if self.player_x.turns[6] else (self.player_y.mark if self.player_y.turns[6] else '')
        eight = self.player_x.mark if self.player_x.turns[7] else (self.player_y.mark if self.player_y.turns[7] else '')
        nine = self.player_x.mark if self.player_x.turns[8] else (self.player_y.mark if self.player_y.turns[8] else '')

        print(f'''
        {one}  |  {two}  |  {three}
        ------------
        {four}  |  {five}  |  {six}
        ------------
        {seven}  |  {eight}  |  {nine}
        ''')

    def check_win(self):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        if self.rounds > 7:
            print('Game Draw')
            return
        for win in wins:
            if self.player_x.turns[win[0]] + self.player_x.turns[win[1]] + self.player_x.turns[win[2]] == 3:
                print(f'{self.player_x.name} Won')
                self.won = True
            elif self.player_y.turns[win[0]] + self.player_y.turns[win[1]] + self.player_y.turns[win[2]] == 3:
                print(f'{self.player_y.name} Won')
                self.won = True

    def start_game(self):

        self.ask_names()
        self.choose_x_or_o()

        while not self.won:
            print(f"{self.player_x.name}'s turn")
            move = int(input("Enter the tile to mark: "))
            self.player_x.turns[move] = 1
            self.grid()
            self.check_win()
            if self.won:
                break
            self.rounds += 1
            if self.rounds > 8:
                break

            print(f"{self.player_y.name}'s turn")
            move = int(input("Enter the tile to mark: "))
            self.player_y.turns[move] = 1
            self.grid()
            self.check_win()
            if self.won:
                break
            self.rounds += 1

            if self.rounds > 8:
                break


class Player:
    def __init__(self,
                 name=None,
                 mark=None
                 ):
        self.name = name
        self.mark = mark
        self.turns = [0, 0, 0, 0, 0, 0, 0, 0, 0]


if __name__ == "__main__":
    print('Working')
    tictactoe = Tictactoe()
    tictactoe.start_game()
