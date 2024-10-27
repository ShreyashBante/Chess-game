import os
import pygame
from board import ChessBoard
# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
LIGHT_BROWN = (244, 164, 96)

# Get the absolute path to the assets folder
ASSETS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets')

# Load piece images
def load_piece_images():
    pieces = ['wp', 'wr', 'wn', 'wb', 'wq', 'wk', 'bp', 'br', 'bn', 'bb', 'bq', 'bk']
    images = {}
    for piece in pieces:
        file_path = os.path.join(ASSETS_PATH, f"{piece}.jpg")  # Change .png to .jpg if you're using jpg files
        if os.path.exists(file_path):
            images[piece] = pygame.transform.scale(pygame.image.load(file_path), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            print(f"Warning: Image file not found: {file_path}")
    return images
piece_images = load_piece_images()

def draw_board(screen):
    for row in range(8):
        for col in range(8):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(screen, board):
    for row in range(8):
        for col in range(8):
            piece = board.board[row][col]
            if piece:
                piece_key = f"{piece.color[0]}{piece.__class__.__name__[0].lower()}"
                screen.blit(piece_images[piece_key], (col * SQUARE_SIZE, row * SQUARE_SIZE))

def main():
    chess_board = ChessBoard()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_board(screen)
        draw_pieces(screen, chess_board)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()