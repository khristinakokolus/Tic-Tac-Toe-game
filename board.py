"""
Represents the module for the board for the game
Method of tree creation is mostly based on the the
algorithm from consultation.
"""
import random
import copy
from btree import LinkedBinaryTree
from btnode import BTNode


class Board:
    """Represents the board for the game"""
    PLAYER_INPUT = "X"
    COMPUTER_INPUT = "0"
    SUPPORTED_MOVES = {"1": (0, 0), "2": (0, 1), "3": (0, 2),
                       "4": (1, 0), "5": (1, 1), "6": (1, 2),
                       "7": (2, 0), "8": (2, 1), "9": (2, 2)}

    def __init__(self):
        """(Board)

        Makes a new board for the game.
        """
        self.board_positions = [[" "] * 3 for _ in range(3)]

    def person_move(self, pos):
        """(Board, tuple)

        Adds person's input to the board.
        """
        if pos in self.free_cells():
            self.board_positions[pos[0]][pos[1]] = Board.PLAYER_INPUT

    def free_cells(self):
        """(Board) -> list

        Returns free moves in the board.
        """
        free_cells = []
        for i in range(3):
            for j in range(3):
                if self.board_positions[i][j] == " ":
                    pos = (i, j)
                    free_cells.append(pos)
        return free_cells

    def check_win(self):
        """(Board) -> str

        Checks who is the winner of the game
        """
        for i in range(3):
            if self.board_positions[i][0] == self.board_positions[i][1] ==\
                    self.board_positions[i][2]:
                return self.board_positions[i][0]
            elif self.board_positions[0][i] == self.board_positions[1][i] ==\
                    self.board_positions[2][i]:
                return self.board_positions[0][i]
        if self.board_positions[0][0] == self.board_positions[1][1] ==\
                self.board_positions[2][2]:
            return self.board_positions[0][0]
        elif self.board_positions[0][2] == self.board_positions[1][1] ==\
                self.board_positions[2][0]:
            return self.board_positions[0][2]
        for item in self.board_positions:
            if " " in item:
                return "no win combination"
        return "no one won"

    def create_tree(self):
        """(Board) -> BTNode

        Creates a tree to find the best move for the
        computer.
        """
        tree = LinkedBinaryTree(BTNode(self.board_positions))
        head_board = BTNode(self)

        def recurse(node, tree, move):
            possible_moves = node.data.free_cells()
            if len(possible_moves) == 1:
                last_board = copy.deepcopy(node)
                if move == "X":
                    next_move = "0"
                else:
                    next_move = "X"
                last_board.data.add(possible_moves[0][0],
                                    possible_moves[0][1], next_move)
                tree.insert_left(last_board)
            else:
                new_first_move = random.choice(possible_moves)
                possible_moves.remove(new_first_move)
                new_second_move = random.choice(possible_moves)

                first_board = copy.deepcopy(node)
                second_board = copy.deepcopy(node)
                if move == "X":
                    next_move = "0"
                else:
                    next_move = "X"

                first_board.data.add(new_first_move[0],
                                     new_first_move[1], next_move)
                second_board.data.add(new_second_move[0],
                                      new_second_move[1], next_move)

                tree.insert_left(first_board)
                tree.insert_right(second_board)

                recurse(first_board, tree.get_left_child(), next_move)
                recurse(second_board, tree.get_right_child(), next_move)

        recurse(head_board, tree, Board.PLAYER_INPUT)
        left_points = self.win_combination_count(tree.get_left_child())
        right_points = self.win_combination_count(tree.get_right_child())
        if left_points > right_points:
            return tree.left_child.key
        return tree.right_child.key

    def win_combination_count(self, tree):
        """(Board) -> int

        Counts win combinations in the left and right
        trees.
        """
        win_count = 0
        tree_leaves_lst = tree.leaves()
        for board in tree_leaves_lst:
            if board.data.check_win() == Board.COMPUTER_INPUT:
                win_count += 1
            elif board.data.check_win() != Board.COMPUTER_INPUT:
                win_count -= 1
        return win_count

    def add(self, i, j, value):
        """(Board, int, int, str)

        Adds the new positions to the board.
        """
        self.board_positions[i][j] = value

    def __str__(self):
        """(Board) -> str

        Returns printable representation of the board
        """
        str_board = ""
        for i in range(3):
            for j in range(3):
                if j == 2:
                    str_board += self.board_positions[i][j] + "\n"
                else:
                    str_board += self.board_positions[i][j] + " | "
            if i != 2:
                str_board += "----------" + "\n"
        return str_board


class BadMoveError(Exception):
    """Exception class for the incorrect input"""
    pass
