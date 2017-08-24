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
        complete_flag = True
        for _ in range(0, 3):
            first_mark = self.board[_][0]
            for i in range(0, self.board_length):
                if self.board[_][i] != first_mark or self.board[_][i] == 0:
                    complete_flag = False
                    break
            if complete_flag:
                self.winner = first_mark
                return True

        complete_flag = True

        # check all vertical rows
        for _ in range(0, 3):
            first_mark = self.board[_][0]
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
