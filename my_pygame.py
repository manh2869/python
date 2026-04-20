import pygame
import random
import drawgrid

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
font = pygame.font.SysFont("Arial", 30)
running = True
draw = True
clock = pygame.time.Clock()
rectx = 24
recty = 24
snakes = [[10, 10], [10, 9]]
direction = "down"
while running:
    screen.fill((255, 255, 255))
    drawgrid.draw_grid(screen, 821, 821, 20)
    fps = clock.get_fps()
    for snake in snakes:
        pygame.draw.rect(screen, (0, 255, 0), (snake[0] * 20, snake[1] * 20, 20, 20))

    if direction == "right":
        snakes.append([snakes[-1][0] + 1, snakes[-1][1]])
        snakes.pop(0)
    if direction == "left":
        snakes.append([snakes[-1][0] - 1, snakes[-1][1]])
        snakes.pop(0)
    if direction == "up":
        snakes.append([snakes[-1][0], snakes[-1][1] - 1])
        snakes.pop(0)
    if direction == "down":
        snakes.append([snakes[-1][0], snakes[-1][1] + 1])
        snakes.pop(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"

    if snakes[-1][0] * 20 == rectx * 10 and snakes[-1][1] * 20 == recty * 10:
        snakes.insert(0, [rectx * 10, recty * 10])
        rectx = random.randrange(20, 80, 2)
        recty = random.randrange(20, 80, 2)

    text1 = font.render(f" {int(fps)}", True, (0, 0, 0))
    textx = font.render(f" {int(snakes[-1][0])}", True, (0, 0, 0))
    texty = font.render(f" {int(snakes[-1][1])}", True, (0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), (rectx * 10, recty * 10, 20, 20))
    screen.blit(text1, (100, 100))
    screen.blit(textx, (700, 100))
    screen.blit(texty, (800, 100))
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
