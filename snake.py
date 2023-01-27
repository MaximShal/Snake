import pygame
import time


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
        self.snake_body_dots = set()
        self.snake_head_dots = set()
        self.snake_length = 1
        self.snake_speed = 10   #Чим менший показник, тим більша швидкість
        self.flag = True

    def dots_of_blocks(self):
        self.snake_body_dots = set()
        self.snake_head_dots = set()
        for k in self.block_list[:-21]:
            for i in range(10):
                self.snake_body_dots.add((k[0] + i, k[1]))
                self.snake_body_dots.add((k[0], k[1] + i))
                self.snake_body_dots.add((k[0] + 10, k[1] + i))
                self.snake_body_dots.add((k[0] + i, k[1] + 10))
        for i in range(10):
            self.snake_head_dots.add((self.block_list[-1][0] + i, self.block_list[-1][1]))
            self.snake_head_dots.add((self.block_list[-1][0], self.block_list[-1][1] + i))
            self.snake_head_dots.add((self.block_list[-1][0] + 10, self.block_list[-1][1] + i))
            self.snake_head_dots.add((self.block_list[-1][0] + i, self.block_list[-1][1] + 10))

    def speed_up(self):
        if self.snake_length != 1 and self.snake_length in [i for i in range(1, 1000, 50)] and self.flag:
            if self.snake_speed <= 2:
                self.snake_speed /= 2
            else:
                self.snake_speed -= 2
            self.flag = False
        elif self.snake_length != 1 and self.snake_length in [i for i in range(1, 1000, 60)]:
            self.flag = True

    def output(self):
        # Малювання змії
        for i in self.block_list:
            pygame.draw.rect(self.screen, self.snake_color, [i[0], i[1], 10, 10])

    def update_snake(self):
        # Оновлення позиції змії
        self.x1 += self.x1_change
        self.y1 += self.y1_change

        # Створення блоку голови змії та видалення блоку хвоста
        snake_head_xy = (self.x1, self.y1)
        self.block_list.append(snake_head_xy)
        if len(self.block_list) > self.snake_length:
            del self.block_list[0]

        # Перезапис крайніх точок всієї зміїї
        self.dots_of_blocks()

        # Збільшення швидкості змії
        if self.snake_speed > 0.001:
            self.speed_up()

        time.sleep(self.snake_speed/1000)

    def up(self):
        self.x1_change = 0
        self.y1_change = -1

    def down(self):
        self.x1_change = 0
        self.y1_change = 1

    def left(self):
        self.x1_change = -1
        self.y1_change = 0

    def right(self):
        self.x1_change = 1
        self.y1_change = 0

    def increase(self):
        self.snake_length += 10

    def snake_death(self):
        # Перевірка зтикання змії з краєм єкрану та хвостом
        if self.x1 + 10 >= self.screen_width or self.x1 < 0 or self.y1 + 10 >= self.screen_height or self.y1 < 0 or \
                len(self.snake_head_dots.intersection(self.snake_body_dots)) != 0:
            return True
        else:
            return False