import unittest
from src.board import ChessBoard

class TestChessBoard(unittest.TestCase):
    def setUp(self):
        self.board = ChessBoard()

    def test_initial_board_setup(self):
        # Test that the initial board is set up correctly
        self.assertIsInstance(self.board.board[1][0], Pawn)
        self.assertIsInstance(self.board.board[0][0], Rook)
        # Add more assertions for initial board state

    def test_move_piece(self):
        # Test moving a piece
        self.assertTrue(self.board.move_piece((1, 0), (2, 0)))  # Move white pawn
        self.assertIsInstance(self.board.board[2][0], Pawn)
        self.assertIsNone(self.board.board[1][0])

    # Add more tests for different scenarios

if __name__ == '__main__':
    unittest.main()