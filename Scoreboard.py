import numpy as np
import math

class Scoreboard:
    __PLAYER_X = "X"
    __PLAYER_O = "O"


    def __init__(self):
        self.__boardArr = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ],
        self.current_player = self.__PLAYER_X

    def start_game(self):
        print(self)
        i = 0
        while i < 10:
            try:
                print(f"Current player - '{self.current_player}'")
                input_index = input("Which position do you want to draw your sign ??")
                result = self.__occupy_position(int(input_index))
                if result:
                    print(f"Player '{self.current_player}' WINS :)")
                    break
                i += 1
            except Exception as message:
                print(message)
                i -= 1

            print(self)
        print(self)

    def __occupy_position(self, position_index):
        if self.__is_position_available(position_index):
            row_index = self.__get_row_index(position_index)
            col_index = self.__get_col_index(position_index, row_index)
            self.__boardArr[0][row_index][col_index] = self.current_player
            # Check if player wins
            if self.__check_if_player_wins():
                return True
            else:
                if self.current_player == self.__PLAYER_O:
                    self.current_player = self.__PLAYER_X
                else:
                    self.current_player = self.__PLAYER_O
                return False
        else:
            raise Exception("Current spot is occupied, choose another one!!!")

            # If no WIN, we change the current player to the other one
    # Check if player wins after its move is performed
    def __check_if_player_wins(self):
        matrix = self.__boardArr[0]
        is_win = self.__check_if_items_are_same(matrix)
        if is_win: return True

        # Transpose matrix and check again
        t_matrix = np.transpose(matrix)
        is_win = self.__check_if_items_are_same(t_matrix)
        if is_win: return True

        #Check if any diagonal is win
        if self.__is_diagonal_win(matrix): return True

        return False

    # Check matrix diagonals for win
    def __is_diagonal_win(self, matrix):
        left_diagonal = [[matrix[0][0], matrix[1][1], matrix[2][2]]]
        check_left = self.__check_if_items_are_same(left_diagonal)

        right_diagonal = [[matrix[0][2], matrix[1][1], matrix[2][0]]]
        check_right = self.__check_if_items_are_same(right_diagonal)
        # If one of it is True we have WIN
        return check_left or check_right

    # Checks if current row items are the same
    def __check_if_items_are_same(self, matrix):
        for i in range(0, len(matrix)):
            items_same = all(j == matrix[i][0] for j in matrix[i])
            if items_same: return True
        return False

    # Checks if selected position is available
    def __is_position_available(self, position_index):
        # Throws exception if number is
        if position_index < 1 or position_index > 9: raise Exception("Entered number is out of board, try again !!!")

        row_index = self.__get_row_index(position_index)
        col_index = self.__get_col_index(position_index, row_index)

        return self.__boardArr[0][row_index][col_index] != self.__PLAYER_X and self.__boardArr[0][row_index][col_index] != self.__PLAYER_O

    def __get_row_index(self, position_index):
        return math.ceil((position_index / 3)) - 1

    def __get_col_index(self, position_index, row_index):
        return position_index - (row_index * 3) - 1



    # Default printing of the board
    def __str__(self):
        matrix = ""
        element_separator = " | "
        new_line = "\n"
        row_separator = "- - - - -"
        for row in self.__boardArr[0]:
            matrix += element_separator.join(row) + new_line

        return matrix
