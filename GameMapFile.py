"""
This file separates all features of the board
Author: James Yoo
"""


# This grid tiles class will represent the board
class GridTiles:
    # constructor to the board gamemap will represent and expect a prebuilt grid/board that will be used in the
    # actual board character_avatar will be the character's in-game character model user_pos was previously going to
    # be some kind of input, but time constraints didn't allow me to complete this feature
    def __init__(self, gamemap, character_avatar, user_pos=None):
        # A premade location for the user to start at
        if user_pos is None:
            user_pos = [14, 6]
        self.gamemap = gamemap
        self.actual_board = []
        self.player_avatar = character_avatar
        self.player_loc = user_pos

    # create the actual board. The board will take the gamemap and reallocate the images from the gamemap onto the
    #actual board
    def create_board(self):
        initial_board_instance = self.actual_board
        for row in range(len(self.gamemap)):
            initial_board_instance.append([])
            for column in range(len(self.gamemap[0])):
                if row == self.player_loc[0] and column == self.player_loc[1]:
                    create_tile = self.player_avatar
                else:
                    create_tile = self.gamemap[row][column]
                initial_board_instance[-1].append(create_tile)
        return initial_board_instance

    #method to print out the grid
    def print_grid(self):
        for row in range(len(self.actual_board)):
            for column in range(len(self.actual_board[0])):
                print(' ', end='')
                print(self.actual_board[row][column], end="  ")
            print("")

    # this method will be used to update movement. Coincidentally my map is filled with trees. So I insured that the
    # only transversable terrain is the square blocks.
    def update_movement(self, movement_choice):
        # use the user's location to keep track of whether a certain direction is valid to move
        user_position_row = self.player_loc[0]
        user_position_col = self.player_loc[1]

        # check if going down is a valid move and if the player is able to move then set the previous spot to square
        # block and update user's avatar
        if self.actual_board[user_position_row + 1][user_position_col] == "⬜" and movement_choice == "s":
            self.player_loc[0] += 1
            self.actual_board[user_position_row][user_position_col] = "⬜"
            self.actual_board[user_position_row + 1][user_position_col] = self.player_avatar
        # check if going up is a valid move and if the player is able to move then set the previous spot to square
        # block and update user's avatar
        elif self.actual_board[user_position_row - 1][user_position_col] == "⬜" and movement_choice == "w":
            self.player_loc[0] -= 1
            self.actual_board[user_position_row][user_position_col] = "⬜"
            self.actual_board[user_position_row - 1][user_position_col] = self.player_avatar
        # check if going left is a valid move and if the player is able to move then set the previous spot to square
        # block and update user's avatar
        elif self.actual_board[user_position_row][user_position_col - 1] == "⬜" and movement_choice == "a":
            self.player_loc[1] -= 1
            self.actual_board[user_position_row][user_position_col] = "⬜"
            self.actual_board[user_position_row][user_position_col - 1] = self.player_avatar
        # check if going right is a valid move and if the player is able to move then set the previous spot to square
        # block and update user's avatar
        elif self.actual_board[user_position_row][user_position_col + 1] == "⬜" and movement_choice == "d":
            self.player_loc[1] += 1
            self.actual_board[user_position_row][user_position_col] = "⬜"
            self.actual_board[user_position_row][user_position_col + 1] = self.player_avatar
