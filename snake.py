import pygame
import time
from random import randint


class Snake:
    def __init__(self, screen, screen_width, screen_height):
        # Ініціалізація змії
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        self.snake_color = (0, 255, 0)
        self.x1 = int(self.screen_width/2)
        self.y1 = int(self.screen_height/2)
        self.x1_change = 0
        self.y1_change = 0
        self.block_list = []
        self.snake_head = []
        self.snake_length = 1
        self.snake_speed = 20   #Чим менший показник, тим більша швидкість
        self.flag = True

    def output(self):
        # Малювання змії
        for i in self.block_list:
            pygame.draw.rect(self.screen, self.snake_color, [i[0], i[1], 10, 10])

    def update_snake(self):
        # Оновлення позиції змії
        self.x1 += self.x1_change
        self.y1 += self.y1_change
        # Створення блоку змії
        self.snake_head = [self.x1, self.y1]
        self.block_list.append(self.snake_head)
        if len(self.block_list) > self.snake_length:
            del self.block_list[0]
        # Збільшення швидкості змії
        if self.snake_length > 1:
            if self.flag and self.snake_length % 25 == 1 and self.snake_speed > 2:
                self.snake_speed -= 2
                print(self.snake_speed)
                self.flag = False
            if self.flag == False and self.snake_length % 30 == 1:
                self.flag = True
        time.sleep(self.snake_speed/1000)

    def up(self):
        self.x1_change = 0
        self.y1_change = -2

    def down(self):
        self.x1_change = 0
        self.y1_change = 2

    def left(self):
        self.x1_change = -2
        self.y1_change = 0

    def right(self):
        self.x1_change = 2
        self.y1_change = 0

    def increase(self):
        self.snake_length += 5

    def snake_death(self):
        if self.x1 >= self.screen_width or self.x1 < 0 or self.y1 >= self.screen_height or self.y1 < 0:
            return True
        else:
            return False


class Food:
    def __init__(self, snake, screen):
        # Ініціалізація їжі
        self.screen = screen
        self.snake = snake
        self.food_color = (255, 0, 0)
        self.food_x = 0
        self.food_y = 0
        self.foods_list = []

    def create_food(self):
        #Створення блоку їжі
        self.food_x = randint(10, self.snake.screen_width-10)
        self.food_y = randint(10, self.snake.screen_height-10)
        for i in self.snake.block_list:
            if self.food_x in list(range(i[0], i[0]+10)) and self.food_y in list(range(i[1], i[1]+10)):
                self.create_food()
            else:
                food_xy = [self.food_x, self.food_y]
                self.foods_list.append(food_xy)

    def draw(self):
        #
        if len(self.foods_list) > 1:
            del self.foods_list[0]
        pygame.draw.rect(self.screen, self.food_color, [self.foods_list[0][0], self.foods_list[0][1], 10, 10])
