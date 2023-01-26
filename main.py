import pygame
import controls
from snake import Snake, Food
import time


def run():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Snake')
    bg_color = (0, 0, 0)
    font_style = pygame.font.SysFont('Arial', 50)
    snake = Snake(screen, screen_width, screen_height)
    food = Food(snake, screen)
    snake.update_snake()
    food.create_food()


    while True:
        controls.events(snake)
        snake.update_snake()
        controls.check_collision(snake, food)
        controls.update(bg_color, screen, snake, food)

        if snake.snake_death():
            msg = font_style.render('DEAD', True, (255, 255, 255))
            screen.blit(msg, [screen_width/2-50, screen_height/2-30])
            pygame.display.update()
            time.sleep(2)
            break


run()
