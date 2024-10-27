from pieces import Pawn, Rook, Knight, Bishop, Queen, King


class ChessBoard:
    def __init__(self):
        self.board = self.create_initial_board()

    
    def create_initial_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        # Set up pawns
        for i in range(8):
            board[1][i] = Pawn('white')
            board[6][i] = Pawn('black')
        # Set up other pieces
        # White pieces
        board[0][0] = Rook('white')
        board[0][1] = Knight('white')
        board[0][2] = Bishop('white')
        board[0][3] = Queen('white')
        board[0][4] = King('white')
        board[0][5] = Bishop('white')
        board[0][6] = Knight('white')
        board[0][7] = Rook('white')
        
        # Black pieces
        board[7][0] = Rook('black')
        board[7][1] = Knight('black')
        board[7][2] = Bishop('black')
        board[7][3] = Queen('black')
        board[7][4] = King('black')
        board[7][5] = Bishop('black')
        board[7][6] = Knight('black')
        board[7][7] = Rook('black')
        
        return board
    


    def is_valid_move(self, start, end):
        # Check if the move is within the board
        if not (0 <= start[0] < 8 and 0 <= start[1] < 8 and 0 <= end[0] < 8 and 0 <= end[1] < 8):
            return False

        piece = self.board[start[0]][start[1]]
        if piece is None:
            return False

        return piece.is_valid_move(self.board, start, end)

    def move_piece(self, start, end):
        if self.is_valid_move(start, end):
            self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = None
            return True
        return False

    def display(self):
        for row in self.board:
            print(' '.join(str(piece) if piece else '.' for piece in row))