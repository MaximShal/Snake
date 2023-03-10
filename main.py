import pygame
import controls
from snake import Snake
from food import Food
from bot import Bot
import time
from threading import Thread


pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')
bg_color = (0, 0, 0)
font_style = pygame.font.SysFont('Arial', 50)

bot = Bot()
thread = Thread(name='bot', target=bot.play)
thread.start()


def run():
    snake = Snake(screen, screen_width, screen_height, bot)
    food = Food(snake, screen)
    bot.update(snake, food)
    snake.update_snake()
    food.create_food()

    while True:
        controls.events(snake, bot)
        snake.update_snake()
        controls.check_collision_food(snake, food)
        controls.update(bg_color, screen, snake, food)

        if snake.snake_death():
            msg = font_style.render('DEAD', True, (255, 255, 255))
            screen.blit(msg, [screen_width/2-50, screen_height/2-30])
            pygame.display.update()
            time.sleep(2)
            break
    run()


run()
