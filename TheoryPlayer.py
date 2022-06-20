"""
NOTES:
Can there be more than one winning move with more than two piles?
"""

class TheoryPlayer:
    def __init__(self, current_board):
        self.board = current_board

    def get_winning_move(self):
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

    def make_winning_move(self):
        """
        Mutate self.board to the resulting state of 
        the board after the winning move is made.
        -1 if the position is losing.
        return: None
        """
        pile_index, num_to_remove = self.get_winning_move()

        if not (pile_index, num_to_remove) == (-1, -1):
            self.board[pile_index] = self.board[pile_index] - num_to_remove

        else:
            print("This is a losing position-- a winning move cannot be made.")


def nim_sum(nums):
    """
    Finds the binary digital sum of a list of ints
    :param nums: (list) values to sum
    return: (int) binary digital sum
    """

    # Base case, return additive identity
    if nums == []:
        return 0

    return nums[-1] ^ nim_sum(nums[:-1])