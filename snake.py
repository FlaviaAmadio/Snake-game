"""
Snake Game in Python using Pygame
Author: Flavia Amadio
Date: 07/08/2025
Description:
    Classic Snake game implementation:
    - Event handling
    - Grid-based movement
    - Collision detection
    - Score tracking and UI rendering

"""


import pygame
import random


def spawn_food():

    """
    Returns a new food position that does not overlap with the snake.
    """

    while True:
        pos = (random.randrange(0, width, cell_size),
               random.randrange(0, height, cell_size))
        if pos not in snake:
            return pos

def show_game_over(screen, score):

    """
    Displays a game over message and final score on the screen.
    """

    font = pygame.font.SysFont(None, 48)
    text = font.render(f"Game Over! Score: {score}", True, WHITE)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait 2 seconds before closing

# --- CONSTANTS AND CONFIGURATION ---

# Screen dimensions
width, height = 600, 400
cell_size = 20

# Colors
BLACK = (0, 0, 0)
MAGENTA = (246, 51, 154)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

# Game settings
fps = 10  # speed of the game

# --- INITIALISATION ---

# Initialize pygame
pygame.init()


# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock
clock = pygame.time.Clock()


# Snake initialisation
snake = [(100, 60), (80, 60), (60, 60)]  # initial body (head first)
direction = (20, 0)  # moving right

# Spawn the first food item at a random grid position
food = spawn_food()

# Set up initial score
score = 0

# --- MAIN GAME LOOP ---

# Game loop
running = True
while running:
    clock.tick(fps)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input for direction changes, and prevent the snake from reversing directly.

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != (20, 0):
        direction = (-20, 0)
    if keys[pygame.K_RIGHT] and direction != (-20, 0):
        direction = (20, 0)
    if keys[pygame.K_UP] and direction != (0, 20):
        direction = (0, -20)
    if keys[pygame.K_DOWN] and direction != (0, -20):
        direction = (0, 20)

    # Move snake
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    snake.insert(0, new_head)

    #print(f"Snake head: {new_head}, Food: {food}")

    # Check collision with food
    if new_head == food:
        score += 1
        print("Ate food! Score:", score)
        food = spawn_food()
    else:
        snake.pop()
    
    # Check collisions with wall or self
    if (new_head[0] < 0 or new_head[0] >= width or
        new_head[1] < 0 or new_head[1] >= height or
        new_head in snake[1:]):
        print("Game Over! Score:", score)
        running = False

# --- DRAWING ---

    # Draw everything
    screen.fill(BLACK)
    # Draw gridlines
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (width, y))

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, cell_size, cell_size))

    pygame.draw.rect(screen, MAGENTA, (*food, cell_size, cell_size))

    #Print score onscreen
    font = pygame.font.SysFont(None, 24)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (5, 5))

    pygame.display.update()

#Show game over screen at the end    
show_game_over(screen, score)
pygame.quit()
