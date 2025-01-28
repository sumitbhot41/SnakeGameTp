import pygame
import sys
import random

WINDOW_SIZE = 600
GRID_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


def draw_grid():
    for x in range(0, WINDOW_SIZE, GRID_SIZE):
        for y in range(0, WINDOW_SIZE, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, (50, 50, 50), rect, 1)

def draw_snake(snake):
    for segment in snake:
        rect = pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, GREEN, rect)

def draw_apple(position):
    rect = pygame.Rect(position[0], position[1], GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, RED, rect)


def game_over():
    font = pygame.font.Font(None, 35)
    message = font.render("Game Over! Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(message, (WINDOW_SIZE // 2 - message.get_width() // 2, WINDOW_SIZE // 2 - 25))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game
                    waiting = False
                    main()
                if event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    sys.exit()


def main():
    snake = [(100, 100), (80, 100), (60, 100)]  # Initial snake position
    direction = (20, 0)  # Initial direction (moving right)
    apple = (200, 200)  # Initial apple position

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, 20):
            direction = (0, -20)
        if keys[pygame.K_DOWN] and direction != (0, -20):
            direction = (0, 20)
        if keys[pygame.K_LEFT] and direction != (20, 0):
            direction = (-20, 0)
        if keys[pygame.K_RIGHT] and direction != (-20, 0):
            direction = (20, 0)

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake = [new_head] + snake[:-1]

        if (
            new_head[0] < 0 or new_head[1] < 0 or
            new_head[0] >= WINDOW_SIZE or new_head[1] >= WINDOW_SIZE or
            new_head in snake[1:]
        ):
            game_over()
            return
        if new_head == apple:
            snake.append(snake[-1])  # Grow the snake
            apple = (
                random.randrange(0, WINDOW_SIZE, GRID_SIZE),
                random.randrange(0, WINDOW_SIZE, GRID_SIZE)
            )

        # Draw everything
        screen.fill(BLACK)
        draw_grid()
        draw_snake(snake)
        draw_apple(apple)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == "__main__":
    main()
