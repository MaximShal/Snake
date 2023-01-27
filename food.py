import pygame
from random import randint


class Food:
    def __init__(self, snake, screen):
        # Ініціалізація їжі
        self.screen = screen
        self.snake = snake
        self.food_color = (255, 0, 0)
        self.food_x = 0
        self.food_y = 0
        self.foods_list = []
        self.block = set()

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

                self.block = set()
                for i in range(10):
                    self.block.add((self.food_x + i, self.food_y))
                    self.block.add((self.food_x, self.food_y + i))
                    self.block.add((self.food_x + 10, self.food_y + i))
                    self.block.add((self.food_x + i, self.food_y + 10))

    def draw(self):
        #Видалення старого блоку їжі, якщо був створений новий та малювання їжі
        if len(self.foods_list) > 1:
            del self.foods_list[0]
        pygame.draw.rect(self.screen, self.food_color, [self.foods_list[0][0], self.foods_list[0][1], 10, 10])
