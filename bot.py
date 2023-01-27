import random
import time


class Bot:
    def __init__(self, snake, food):
        # Ініціалізація бота
        self.snake = snake
        self.food = food
        self.complexity = 100
        self.flag_game = True
        self.bot_frequency = (0.25, 0.75)
        self.sides = {'left': snake.left,
                      'right': snake.right,
                      'up': snake.up,
                      'down': snake.down}
        self.snake_radar_size = [(self.snake.x1-25, self.snake.x1+25), (self.snake.y1-25, self.snake.y1+25)]

    # Перевірка руху "тільки не йти назад"
    def not_back(self):
        try:
            if (self.snake.block_list[-1][0]+1, self.snake.block_list[-1][1]) == self.snake.block_list[-2]:
                return ['left', 'down', 'up']
            elif (self.snake.block_list[-1][0]-1, self.snake.block_list[-1][1]) == self.snake.block_list[-2]:
                return ['right', 'up', 'down']
            elif (self.snake.block_list[-1][0], self.snake.block_list[-1][1]+1) == self.snake.block_list[-2]:
                return ['left', 'up', 'right']
            elif (self.snake.block_list[-1][0], self.snake.block_list[-1][1]-1) == self.snake.block_list[-2]:
                return ['right', 'down', 'left']
            else:
                return ['right', 'down', 'left', 'up']
        except IndexError:
            return ['right', 'down', 'left', 'up']

    def true_way_chek(self, way):
        not_back = self.not_back()
        if way in not_back:
            self.sides[way]()
        else:
            self.sides[not_back[random.randint(0, len(not_back) - 1)]]()

    def true_going(self):
        if self.snake.block_list[-1][0] + 5 > self.food.food_x + 5 and self.snake.block_list[-1][1] + 5 > \
                self.food.food_y + 5:
            # 'зліва зверху'
            if (self.snake.block_list[-1][0] + 5) - (self.food.food_x + 5) > (self.snake.block_list[-1][1] + 5) - (
                    self.food.food_y + 5):
                self.true_way_chek('left')
            else:
                self.true_way_chek('up')

        elif self.snake.block_list[-1][0] + 5 < self.food.food_x + 5 and self.snake.block_list[-1][
            1] + 5 > self.food.food_y + 5:
            # 'зправа зверху'
            if (self.food.food_x + 5) - (self.snake.block_list[-1][0] + 5) > (self.snake.block_list[-1][1] + 5) - (
                    self.food.food_y + 5):
                self.true_way_chek('right')
            else:
                self.true_way_chek('up')

        elif self.snake.block_list[-1][0] + 5 > self.food.food_x + 5 and self.snake.block_list[-1][
            1] + 5 < self.food.food_y + 5:
            # 'зліва знизу'
            if (self.snake.block_list[-1][0] + 5) - (self.food.food_x + 5) > (self.food.food_y + 5) - (
                    self.snake.block_list[-1][1] + 5):
                self.true_way_chek('left')
            else:
                self.true_way_chek('down')

        elif self.snake.block_list[-1][0] + 5 < self.food.food_x + 5 and self.snake.block_list[-1][
            1] + 5 < self.food.food_y + 5:
            # 'зправа знизу'
            if (self.food.food_x + 5) - (self.snake.block_list[-1][0] + 5) > (self.food.food_y + 5) - (
                    self.snake.block_list[-1][1] + 5):
                self.true_way_chek('right')
            else:
                self.true_way_chek('down')

    def play(self):
        while self.flag_game:
            time.sleep(random.uniform(self.bot_frequency[0], self.bot_frequency[1]))

            # Оновлення положення радару
            self.snake_radar_size = [(self.snake.x1-25, self.snake.x1+25), (self.snake.y1-25, self.snake.y1+25)]

            # Перевірка вірогідності виконання правильного шляху
            chance = random.randint(1, 1000)
            if chance <= self.complexity * 10:
                # if self.snake_radar_size[0][0] < self.food.food_x+5 < self.snake_radar_size[0][1] and self.snake_radar_size[1][0] < self.food.food_y+5 < self.snake_radar_size[1][1]:
                food_xy = [self.food.food_x, self.food.food_y]
                while food_xy == self.food.foods_list:
                    self.true_going()
                # else:
                self.true_going()
            else:
                self.sides[self.not_back()[random.randint(0, len(self.not_back())-1)]]()

    def end(self, flag):
        if not flag:
            self.flag_game = False
