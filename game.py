"""Module that represents the module for game simulation"""
from board import Board, BadMoveError


def play():
    """
    Represents the simulation of the tic-tac-toe
    game.
    """
    board = Board()
    while True:
        player_position = player_move(board)
        board.person_move(player_position)
        print("Your move:")
        print(board)
        print()
        if board.check_win() == board.PLAYER_INPUT:
            winner = board.PLAYER_INPUT
            return winner
        if board.check_win() == "no one won":
            winner = "no one won"
            return winner
        board.board_positions = board.create_tree().data.board_positions
        print("Computer's move:")
        print(board)
        if board.check_win() == board.COMPUTER_INPUT:
            winner = board.COMPUTER_INPUT
            return winner


def player_move(board):
    """
    Controls the input of the user
    """
    free_cells = [sublist for sublist in board.free_cells()]
    pos_value = input("Please input the position you want: ")
    while pos_value not in board.SUPPORTED_MOVES.keys() or\
            board.SUPPORTED_MOVES[pos_value] not in free_cells:
        try:
            raise BadMoveError
        except BadMoveError:
            print("Your input value is wrong! Try again!")
            pos_value = input("Please input the position you want: ")
    print()
    position = board.SUPPORTED_MOVES[pos_value]
    return position


def main():
    """
    Main function to lead the game.
    """
    print("Welcome to the Tic-Tac-Toe game!")
    print("You will play against the computer.")
    print("So, let's start.")
    print("First choose a cell numbered from 1 to 9 as below and play.")
    initial_board = "1 | 2 | 3" + "\n" + "----------" + "\n" +\
                    "4 | 5 | 6" + "\n" + "----------" + "\n" +\
                    "7 | 8 | 9" + "\n"
    print(initial_board)
    print("- - - - - - - - ")
    print()
    winner = play()
    if winner == "X":
        print("You won the game!")
    elif winner == "0":
        print("Unfortunately, you lost the game!")
    elif winner == "no one won":
        print("No one won the game.")


main()
