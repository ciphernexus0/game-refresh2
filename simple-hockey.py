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
puck = pygame.Rect(WIDTH // 2 - PUCK_SIZE // 2, HEIGHT // 2 - PUCK_SIZE // 2, PUCK_SIZE, PUCK_SIZE)

# Puck velocity
puck_velocity = [PUCK_SPEED, PUCK_SPEED]

# Scores
score1 = 0
score2 = 0

# Font for displaying score
font = pygame.font.Font(None, 74)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += PADDLE_SPEED

    # Move the puck
    puck.x += puck_velocity[0]
    puck.y += puck_velocity[1]

    # Collision with walls
    if puck.top <= 0 or puck.bottom >= HEIGHT:
        puck_velocity[1] = -puck_velocity[1]

    # Collision with paddles
    if puck.colliderect(player1) or puck.colliderect(player2):
        puck_velocity[0] = -puck_velocity[0]

    # Scoring
    if puck.left <= 0:
        score2 += 1
        puck.center = (WIDTH // 2, HEIGHT // 2)
        puck_velocity = [PUCK_SPEED, PUCK_SPEED]
    if puck.right >= WIDTH:
        score1 += 1
        puck.center = (WIDTH // 2, HEIGHT // 2)
        puck_velocity = [-PUCK_SPEED, -PUCK_SPEED]

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, BLUE, player2)
    pygame.draw.ellipse(screen, WHITE, puck)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Draw scores
    score_text = font.render(f"{score1} : {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 50, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
