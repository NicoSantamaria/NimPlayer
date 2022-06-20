class NimGame:
    
    def __init__(self, nim_board):
        """ CONSTRUCTOR """

        self.board = nim_board[:]

    def make_move(self, pile, num):
        """
        If move is valid, removes num from pile and returns True.
        Otherwise, returns Talse. 
        """
        if 0 <= pile < len(self.board) - 1:

            if num < self.board[pile]:

                self.board[pile] = self.board[pile] - num
                return True

        return False

    def get_board(self):
        """ Access board state """
        return self.board
