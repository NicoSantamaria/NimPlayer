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

    def get_next_states(self):
        """
        Find all possible moves from the current state
        """
        next_states = []

        # Find every combination of piles and num to remove from piles
        for x in range(len(self.board)):
            for y in range(1, self.board[x] + 1):

                # Append every resulting 
                next_state = self.board[:]
                next_state[x] = next_state[x] - y
                next_states.append(next_state)
