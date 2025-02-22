import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Hockey Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game settings
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
PUCK_SIZE = 20
PADDLE_SPEED = 8
PUCK_SPEED = 6

# Initialize paddles and puck
player1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
puck = pygame.Rect(WIDTH // 2 - PUCK_SIZE // 2, HEIGHT // 2 - PUCK_SIZE // 2,
