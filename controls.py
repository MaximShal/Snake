import pygame
import sys


def events(snake):
    # Івенти натискання кнопок, для тесту(можна погратись)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
    if (snake.x1 in list(range(food.food_x, food.food_x + 10)) and snake.y1 in list(
            range(food.food_y, food.food_y + 10)) or
            snake.x1 + 10 in list(range(food.food_x, food.food_x + 10)) and snake.y1 in list(
                range(food.food_y, food.food_y + 10)) or
            snake.x1 in list(range(food.food_x, food.food_x + 10)) and snake.y1 + 10 in list(
                range(food.food_y, food.food_y + 10)) or
            snake.x1 + 10 in list(range(food.food_x, food.food_x + 10)) and snake.y1 + 10 in list(
                range(food.food_y, food.food_y + 10))):
        food.create_food()
        snake.increase()
