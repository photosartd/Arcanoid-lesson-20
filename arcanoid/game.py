import pygame
from platform import Platform
from platform import Wall
from Circle import Circle

pygame.init()
#win - Surface
win_size = 500
win = pygame.display.set_mode((win_size, win_size))
background_color = (0,0,0)
platform_color = (255,0,0)

platform = Platform(win, win_size, platform_color)
ball_center = (win_size/2, win_size/2)
ball_radius = win_size/50
ball_color = (255,0,0)
ball = Circle(ball_color, ball_radius, ball_center)
wall = Wall(win, win_size, platform_color)
bricks_rows = 3
bricks_cols = 5
wall.fill_bricks(bricks_rows, bricks_cols)
FPS = 60
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(background_color)
    #code
    ball.random_movement(win_size, platform, wall)
    wall.draw()
    ball.draw(win)
    platform.move_by_keys()
    platform.draw()

    pygame.display.update()
    clock.tick(FPS)