
# --- Clean working version ---
import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake - Nokia 1200 Style')
clock = pygame.time.Clock()

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

def move_snake(snake, direction):
    head_x, head_y = snake[0]
    new_head_x = (head_x + direction[0] * CELL_SIZE) % WIDTH
    new_head_y = (head_y + direction[1] * CELL_SIZE) % HEIGHT
    new_head = (new_head_x, new_head_y)
    snake.insert(0, new_head)
    return snake

def check_collision(snake):
    head = snake[0]
    if head in snake[1:]:
        return True
    return False

def main():
    direction = RIGHT
    while True:
        snake = [(WIDTH // 2, HEIGHT // 2)]
        direction = RIGHT
        score = 0
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        running = True
        while running:
            clock.tick(6)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != DOWN:
                        direction = UP
                    elif event.key == pygame.K_DOWN and direction != UP:
                        direction = DOWN
                    elif event.key == pygame.K_LEFT and direction != RIGHT:
                        direction = LEFT
                    elif event.key == pygame.K_RIGHT and direction != LEFT:
                        direction = RIGHT

            snake[:] = move_snake(snake, direction)
            if snake[0] == food:
                score += 1
                food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
            else:
                snake.pop()

            if check_collision(snake):
                font = pygame.font.SysFont(None, 36)
                text = font.render(f'Game Over! Score: {score}', True, WHITE)
                screen.fill(BLACK)
                screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
                pygame.display.flip()
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            waiting = False
                running = False
            else:
                screen.fill(BLACK)
                draw_snake(snake)
                draw_food(food)
                pygame.display.flip()

if __name__ == '__main__':
    main()
