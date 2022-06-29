from copy import deepcopy


class SearchPlayer:
    
    def __init__(self, nim_board, turn=True):
        self.board = nim_board[:]
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

    def get_next_states(self):
        """
        Find all possible moves from the current state.
        """
        next_states = []

        # Find every combination of piles and num to remove from piles
        for x in range(len(self.board)):
            for y in range(1, self.board[x] + 1):

                # Create and append every resulting board to a list
                next_state = deepcopy(self)
                next_state.board[x] = next_state.board[x] - y
                next_state.change_player_turn()
                next_states.append(next_state)

        return next_states

    def is_over(self):
        """
        Determines if game has ended.
        """
        return self.board == [0] * len(self.board)

    def get_next_board(self):
        """
        Calls the recursive search to generate a list of
        winning next moves.
        """
        winning_moves = []

        for state in self.get_next_states():
            if adversarial_search(state) == 1:
                winning_moves.append(state.board)

        if winning_moves == []:
            print("This is a losing position-- a winning move cannot be made.")

        return winning_moves

    def score(self):
        """
        Score for adversarial search.
        """
        if self.player_turn:
            return -1
        else:
            return 1

    def __str__(self):
        return str(self.board) + "\n" + str(self.player_turn)


def adversarial_search(state):
    """
    Determines whether a game-state is winning.
    :param state: (SearchPlayer object)
    return: (int) 1 if winning, -1 if not
    """
    if state.is_over():
        return state.score()

    results = []

    for s in state.get_next_states():
        results.append(adversarial_search(s))

    if state.player_turn:
        return max(results)

    return min(results)