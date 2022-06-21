from NimGame import *
from TheoryPlayer import *


def Search(board):
    return


def main():
    
    print("Welcome! Please input each pile you would like to see in the " \
        + "\nnim game followed by the enter key. Input nothing to finish." \
        + "\nFor instance, 4,6,5, followed by nothing would create a game " \
        + "\nwith piles of 4, 6, and 5.")

    start_state = []
    pile_input = input("Please input the pile you would like to add. Empty string finishes.\n")

    while pile_input != "":
        start_state.append(int(pile_input))
        pile_input = input("Please input the pile you would like to add. Empty string finishes.\n")

    theory = TheoryPlayer(start_state)
    print(theory.get_winning_move())


if __name__ == "__main__":
    main()
