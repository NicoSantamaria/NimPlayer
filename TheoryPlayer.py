"""
NOTES:
Can there be more than one winning move with more than two piles?

From Math Stack Exchange: 
There are always an odd number of winning moves, and at most one such move in each pile.

So for a game of two piles, there is only one winning move. But in games of three piles, for instance,
there might be 1 or 3 winning moves. And so on for larger piles numbers. 
"""
from copy import deepcopy


class TheoryPlayer:

    def __init__(self, nim_board, turn=True):
        self.board = nim_board
        self.player_turn = turn

    def change_player_turn(self):
        self.player_turn = not self.player_turn

    def make_move(self, pile, num):
        """
        If move is valid, removes num from pile.
        Otherwise, prints error message.
        """
        self.change_player_turn()

        if 0 <= pile < len(self.board) - 1:
            if num < self.board[pile]:
                self.board[pile] = self.board[pile] - num

        print("That is not a valid move.")

    def get_next_move(self):
        """
        Find the moves that result in a board with nim-sum zero. Returns -1, -1 if
        the position is not winning
        return: (tuple) pile and num to remove resulting nim-sum zero
        """
        board_sum = nim_sum(self.board)

        # Find appropriate pile and number to remove
        pile_index = 0

        for pile_size in self.board:

            # If the appropriate pile, this is how many objects should remain
            size_to_move = nim_sum([board_sum, pile_size])
            
            # Find appropriate pile (see theory page)
            if size_to_move < pile_size:
                return pile_index, pile_size - size_to_move
            
            pile_index += 1

        return -1, -1

    def get_next_board(self):
        """
        Returns the board that results after making the next move
        """
        next_board = deepcopy(self)
        pile, num = next_board.get_next_move()
        next_board.make_move(pile, num)

        return [next_board.board]


def nim_sum(nums):
    """
    Finds the binary digital sum of a list of ints
    :param nums: (list) values to sum
    return: (int) binary digital sum
    """
    if nums == []:
        return 0

    return nums[-1] ^ nim_sum(nums[:-1])