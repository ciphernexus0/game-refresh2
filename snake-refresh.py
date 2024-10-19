import pygame
import random

# Initialize pygame
pygame.init()

# Game window dimensions
WIDTH, HEIGHT = 640, 480
BLOCK_SIZE = 20
FPS = 10

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Enhanced Snake Game')

# Clock for controlling FPS
clock = pygame.time.Clock()

# Function to display the player's score
def show_score(score):
    value = score_font.render(f"Your Score: {score}", True, BLUE)
    screen.blit(value, [0, 0])

# Function to draw the snake on the screen
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])

# Function to show a message on the screen (for Game Over, etc.)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial snake position
    x = WIDTH / 2
    y = HEIGHT / 2

    # Change in position
    x_change = 0
    y_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # Obstacle positions
    obstacles = []
    for _ in range(5):  # Add 5 random obstacles
        obs_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        obs_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        obstacles.append([obs_x, obs_y])

    score = 0

    # Main game loop
    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press C-Play Again or Q-Quit", RED)
            show_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle user input for snake direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        # Move snake
        x += x_change
        y += y_change

        # Check for collisions with the boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Check for collisions with the obstacles
        for obs in obstacles:
            if x == obs[0] and y == obs[1]:
                game_close = True

        # Update the screen
        screen.fill(BLACK)

        # Draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Draw obstacles
        for obs in obstacles:
            pygame.draw.rect(screen, BLUE, [obs[0], obs[1], BLOCK_SIZE, BLOCK_SIZE])

        # Update the snake's position and check for growth
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake collides with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        show_score(score)

        # Check if the snake eats the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1
            score += 1
            FPS += 1  # Increase speed as the score increases

        pygame.display.update()

        # Control the game's speed
        clock.tick(FPS)

    pygame.quit()
    quit()

# Run the game
game_loop()
