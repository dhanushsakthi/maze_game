import pygame
import random
import sys

ROWS, COLS = 15, 15     
CELL_SIZE = 40          
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Maze Game")
clock = pygame.time.Clock()

DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def generate_maze(grid, x, y):
    grid[y][x] = 1  
    random.shuffle(DIRS)
    for dx, dy in DIRS:
        nx, ny = x + dx * 2, y + dy * 2
        if 0 <= nx < COLS and 0 <= ny < ROWS and grid[ny][nx] == 0:
            grid[y + dy][x + dx] = 1  
            generate_maze(grid, nx, ny)

def draw_maze(grid, player_pos, goal_pos):
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[y][x] == 1:
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)
    px, py = player_pos
    pygame.draw.rect(screen, BLUE, (px * CELL_SIZE, py * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    gx, gy = goal_pos
    pygame.draw.rect(screen, GREEN, (gx * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
  
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    generate_maze(grid, 0, 0)

    player_pos = [0, 0]
    goal_pos = [COLS - 1, ROWS - 1]

    running = True
    won = False
    while running:
        screen.fill(BLACK)
        draw_maze(grid, player_pos, goal_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not won:
                x, y = player_pos
                if event.key == pygame.K_UP and y > 0 and grid[y - 1][x] == 1:
                    player_pos[1] -= 1
                if event.key == pygame.K_DOWN and y < ROWS - 1 and grid[y + 1][x] == 1:
                    player_pos[1] += 1
                if event.key == pygame.K_LEFT and x > 0 and grid[y][x - 1] == 1:
                    player_pos[0] -= 1
                if event.key == pygame.K_RIGHT and x < COLS - 1 and grid[y][x + 1] == 1:
                    player_pos[0] += 1

       
        if player_pos == goal_pos:
            won = True
            font = pygame.font.SysFont(None, 55)
            text = font.render('You Win!', True, RED)
            screen.blit(text, (WIDTH // 3, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()



