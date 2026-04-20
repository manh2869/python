import pygame


def draw_grid(screen, width, height, cell_size):
    color = (0, 0, 0)
    for x in range(200, width, cell_size):
        pygame.draw.line(screen, color, (x, 200), (x, height))

    for y in range(200, height, cell_size):
        pygame.draw.line(screen, color, (200, y), (width, y))
