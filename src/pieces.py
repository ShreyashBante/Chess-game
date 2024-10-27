class Piece:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, board, start, end):
        raise NotImplementedError("Subclass must implement abstract method")

    def __str__(self):
        return f"{self.color[0]}{self.__class__.__name__[0]}"

class Pawn(Piece):
    def is_valid_move(self, board, start, end):
        start_row, start_col = start
        end_row, end_col = end
        
        # Direction of movement (1 for white, -1 for black)
        direction = 1 if self.color == 'white' else -1
        
        # Check if moving forward
        if start_col == end_col:
            # Moving one square forward
            if end_row == start_row + direction:
                return board[end_row][end_col] is None
            # Moving two squares forward from starting position
            elif (self.color == 'white' and start_row == 1 and end_row == 3) or \
                 (self.color == 'black' and start_row == 6 and end_row == 4):
                return board[end_row][end_col] is None and board[start_row + direction][start_col] is None
        
        # Check if capturing diagonally
        elif abs(start_col - end_col) == 1 and end_row == start_row + direction:
            return board[end_row][end_col] is not None and board[end_row][end_col].color != self.color
        
        return False

class Rook(Piece):
    def is_valid_move(self, board, start, end):
        start_row, start_col = start
        end_row, end_col = end
        
        # Check if moving in a straight line
        if start_row != end_row and start_col != end_col:
            return False
        
        # Check if path is clear
        row_step = 0 if start_row == end_row else (1 if end_row > start_row else -1)
        col_step = 0 if start_col == end_col else (1 if end_col > start_col else -1)
        
        current_row, current_col = start_row + row_step, start_col + col_step
        while (current_row, current_col) != (end_row, end_col):
            if board[current_row][current_col] is not None:
                return False
            current_row += row_step
            current_col += col_step
        
        # Check if destination is empty or contains an opponent's piece
        return board[end_row][end_col] is None or board[end_row][end_col].color != self.color

class Knight(Piece):
    def is_valid_move(self, board, start, end):
        start_row, start_col = start
        end_row, end_col = end
        
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        # Knight moves in an L-shape
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            return board[end_row][end_col] is None or board[end_row][end_col].color != self.color
        
        return False

class Bishop(Piece):
    def is_valid_move(self, board, start, end):
        start_row, start_col = start
        end_row, end_col = end
        
        # Check if moving diagonally
        if abs(end_row - start_row) != abs(end_col - start_col):
            return False
        
        # Check if path is clear
        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1
        
        current_row, current_col = start_row + row_step, start_col + col_step
        while (current_row, current_col) != (end_row, end_col):
            if board[current_row][current_col] is not None:
                return False
            current_row += row_step
            current_col += col_step
        
        # Check if destination is empty or contains an opponent's piece
        return board[end_row][end_col] is None or board[end_row][end_col].color != self.color

class Queen(Piece):
    def is_valid_move(self, board, start, end):
        # Queen combines Rook and Bishop movements
        rook = Rook(self.color)
        bishop = Bishop(self.color)
        return rook.is_valid_move(board, start, end) or bishop.is_valid_move(board, start, end)

class King(Piece):
    def is_valid_move(self, board, start, end):
        start_row, start_col = start
        end_row, end_col = end
        
        # King can move one square in any direction
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        if row_diff <= 1 and col_diff <= 1:
            return board[end_row][end_col] is None or board[end_row][end_col].color != self.color
        
        return False