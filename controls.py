import pygame
import sys


def events(snake, bot):
    # Івенти натискання кнопок, для тесту(можна погратись)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bot.end(False)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.up()
            elif event.key == pygame.K_DOWN:
                snake.down()
            elif event.key == pygame.K_LEFT:
                snake.left()
            elif event.key == pygame.K_RIGHT:
                snake.right()


def update(bg_color, screen, snake, food):
    # оновлення екрану
    screen.fill(bg_color)
    snake.output()
    food.draw()
    pygame.display.flip()


def check_collision(snake, food):
    if len(snake.snake_head_dots.intersection(food.block)) != 0:
        food.create_food()
        snake.increase()