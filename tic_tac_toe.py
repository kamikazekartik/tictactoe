# playing tic tac toe
import numpy as np

board_states = np.zeros(2^9)

class TictactoeBoard:
    def __init__(self):
        # create an empty board
        self.board = np.zeros([3, 3])
        self.complete = False
        self.board_length = 3
        self.winner = None

    def is_complete(self):
        # check all horizontal rows
        for _ in range(0, 3):
            complete_flag = True
            first_mark = self.board[_][0]
            for i in range(0, self.board_length):
                if self.board[_][i] != first_mark or self.board[_][i] == 0:
                    complete_flag = False
                    break
            if complete_flag:
                self.winner = first_mark
                return True

        # check all vertical rows
        for _ in range(0, 3):
            complete_flag = True
            first_mark = self.board[0][_]
            for i in range(0, self.board_length):
                if self.board[i][_] != first_mark or self.board[i][_] == 0:
                    complete_flag = False
                    break
            if complete_flag:
                self.winner = first_mark
                return True


        complete_flag = True
        # check diagonal rows
        first_mark = self.board[0][0]
        for i in range(0, self.board_length-1):
            if self.board[i+1][i+1] != first_mark or self.board[i+1][i+1] == 0:
                complete_flag = False
                break
        if complete_flag:
            self.winner = first_mark
            return True

        complete_flag = True
        first_mark = self.board[self.board_length-1][0]
        for i in range(1, self.board_length):
            if self.board[self.board_length-1-i][i] != first_mark or self.board[self.board_length-1-i][i] == 0:
                complete_flag = False
                break
        if complete_flag:
            self.winner = first_mark
            return True
        
        # check if there are any empty slots
        complete_flag = True
        for i in range(0, self.board_length):
            for j in range(0, self.board_length):
                if self.board[i][j] == 0.0:
                    complete_flag = False
        return complete_flag

    def print_board(self):
        board_str = ""
        for i in range(0, self.board_length):
            for j in range(0, self.board_length):
                if self.board[i][j] == 0:
                    item = ' '
                else:
                    item = str(int(self.board[i][j]))
                if j < (self.board_length - 1):
                    board_str += item + " | "
                else:
                    board_str += item + "\n"
        print board_str


class Game:
    def __init__(self):
        self.empty = True
        self.board = None
        self.totem_list = [1, 2]
        # Note that epoch changes only when a successful move is played
        # also player = (epoch%2 + 1)
        self.epoch = None
        
    def start_game(self):
        self.board = TictactoeBoard()
        self.epoch = 1
        while not self.board.is_complete():
            self.epoch += 1
            print "epoch!", self.epoch
            totem = self.totem_list[self.epoch%2]
            print "totem!", totem
            self.get_input(totem)
            self.board.print_board()
        
        if self.board.winner:
            print "Congratulations player {} you are the winner!".format(self.epoch%2 + 1)
        else:
            print "Aww.. It's a tie"
            
    def get_coordinates_from_input(self, loc):
        coordinates_loc_map = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                              '4': (1, 0), '5': (1, 1), '6': (1, 2),
                              '7': (2, 0), '8': (2, 1), '9': (2, 2),}
        return coordinates_loc_map.get(loc)

    def get_input(self, totem=1):
        print "Player {}. Your move!".format(self.epoch%2 + 1)
        print "Please enter your move as a number between 1-9"
        print "(1 is the first square, 2 is the second and so on.)"
        loc = raw_input()
        (x, y) = self.get_coordinates_from_input(loc)
        if self.play_move(x, y, totem):
            return
        else:
            print "Invalid input, try again"
            self.get_input(totem)
        
    def play_move(self, x, y, totem=1):
        if self.board.board[x][y] != 0:
            return False
        self.board.board[x][y] = totem
        return True
