import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Window size and cell size
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control the game frame rate
clock = pygame.time.Clock()

# Font for displaying the score
font = pygame.font.SysFont(None, 36)

def draw_snake(snake):
    """Draws each segment of the snake"""
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(position):
    """Draws the food on the screen"""
    pygame.draw.rect(screen, RED, (position[0], position[1], CELL_SIZE, CELL_SIZE))

def show_score(score):
    """Displays the current score"""
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, [10, 10])

def game_loop():
    """Main game loop that runs the snake game"""
    # Initialize the snake in the center of the screen
    snake = [[WIDTH // 2, HEIGHT // 2]]
    # Initial direction: moving to the right
    direction = [CELL_SIZE, 0]
    # Place food at a random position
    food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
    score = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Change direction based on arrow keys, disallow reversing direction
                if event.key == pygame.K_LEFT and direction != [CELL_SIZE, 0]:
                    direction = [-CELL_SIZE, 0]
                elif event.key == pygame.K_RIGHT and direction != [-CELL_SIZE, 0]:
                    direction = [CELL_SIZE, 0]
                elif event.key == pygame.K_UP and direction != [0, CELL_SIZE]:
                    direction = [0, -CELL_SIZE]
                elif event.key == pygame.K_DOWN and direction != [0, -CELL_SIZE]:
                    direction = [0, CELL_SIZE]

        # Move the snake by creating a new head based on the current direction
        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        snake.insert(0, new_head)

        # Check for wall collisions
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            break
        # Check for self-collision
        if new_head in snake[1:]:
            break

        # Check if the snake has eaten the food
        if new_head == food:
            score += 1
            # Place new food at a random position
            food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
        else:
            # Remove the last segment of the snake if no food has been eaten
            snake.pop()

        # Fill the screen with black to clear previous frames
        screen.fill(BLACK)
        # Draw the snake and the food
        draw_snake(snake)
        draw_food(food)
        # Display the score
        show_score(score)
        # Update the display
        pygame.display.flip()
        # Limit the game to 10 frames per second
        clock.tick(10)

    # Quit Pygame when the loop ends
    pygame.quit()

if __name__ == "__main__":
    game_loop()
  
