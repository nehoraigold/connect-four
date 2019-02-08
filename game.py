from player import Player
from board import Board
import random
import os


class Game():
    def __init__(self):
        self.rules()
        self.player_1, self.player_2 = Player.init_players()
        self.board = Board()
        self.active_player = self.randomly_select_starting_player()
        self.start()

    def start(self):
        input("\nPress any key to start!")
        while not self.complete():
            os.system('cls')
            self.print_turn_header(self.active_player)
            self.board.display()
            col = self.board.select_valid_column()
            self.board.add_marker(self.active_player, col)
            self.change_active_player()
        self.end()

    def print_turn_header(self, player):
        turn_title = "{}'s Turn".format(player.name)
        self.print_header(turn_title)

    def print_header(self, title):
        border = "=" * (8 + len(title)) + "\n"
        header = "{0}||  {1}  ||\n{0}".format(border, title)
        print(header)

    def randomly_select_starting_player(self):
        starting_player = random.choice([self.player_1, self.player_2])
        print("\nGreat! It's been randomly determined that {} will go first.".format(
            starting_player.name))
        return starting_player

    def change_active_player(self):
        self.active_player = self.player_1 if self.active_player == self.player_2 else self.player_2

    def complete(self):
        return self.board.is_full() or self.board.has_connect_four()

    def rules(self):
        os.system('cls')
        self.print_header("CONNECT FOUR")
        print("Objective: To win Connect Four you must be the first player to get four of your markers in a row either horizontally, vertically or diagonally.\n")

    def end(self):
        os.system('cls')
        if self.board.has_connect_four():
            self.change_active_player()
            self.print_header("{} Wins".format(self.active_player.name))
        else:
            self.print_header("Draw")
        self.board.display()

    def play_again(self):
        self.again = input("\nWould you like to play again? ").lower()
        YES_ANSWERS = ['y', 'yes']
        NO_ANSWERS = ['n', 'no']
        while self.again not in YES_ANSWERS and self.again not in NO_ANSWERS:
            self.play_again()
        return self.again in YES_ANSWERS
