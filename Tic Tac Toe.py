import pygame
import sys

pygame.init()

screen_size = 600
cell_size = screen_size // 3
font_size = 100

screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Tic-Tac-Toe")


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)


board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False


font = pygame.font.SysFont(None, font_size)

def draw_board():
    screen.fill(white)
    for row in range(1, 3):
        pygame.draw.line(screen, black, (0, row * cell_size), (screen_size, row * cell_size), 5)
    for col in range(1, 3):
        pygame.draw.line(screen, black, (col * cell_size, 0), (col * cell_size, screen_size), 5)
    
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                text_surface = font.render("X", True, red)
                text_rect = text_surface.get_rect(center=((col * cell_size) + cell_size // 2, (row * cell_size) + cell_size // 2))
                screen.blit(text_surface, text_rect)
            elif board[row][col] == "O":
                text_surface = font.render("O", True, blue)
                text_rect = text_surface.get_rect(center=((col * cell_size) + cell_size // 2, (row * cell_size) + cell_size // 2))
                screen.blit(text_surface, text_rect)

def check_winner():
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]

    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    return None

def is_draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                return False
    return True

def show_winner(winner=None):
    font = pygame.font.SysFont(None, 100)
    if winner:
        message = f"Player {winner} Wins!"
    else:
        message = "Match Draw!"
    
    text_surface = font.render(message, True, black)
    text_rect = text_surface.get_rect(center=(screen_size // 2, screen_size // 2))
    
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)  


running = True
while running:
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row, col = y // cell_size, x // cell_size

            if board[row][col] == "":
                board[row][col] = current_player
                winner = check_winner()
                if winner:
                    game_over = True
                    show_winner(winner)
                elif is_draw():
                    game_over = True
                    show_winner()
                else:
                    current_player = "O" if current_player == "X" else "X"

pygame.quit()
sys.exit()
