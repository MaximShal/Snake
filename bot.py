import random
import time


class Bot:
    def __init__(self):
        # Ініціалізація бота
        self.sides = None
        self.food = None
        self.snake = None
        self.flag_game = True
        self.flag_tail = False
        self.bot_frequency = (0.2, 0.3)
        self.test = set()

    # Передача нових обєктів змії та їжі боту
    def update(self, snake, food):
        self.snake = snake
        self.food = food
        self.sides = {'left': snake.left,
                      'right': snake.right,
                      'up': snake.up,
                      'down': snake.down}

    # Перевірка зтикання
    def exceptions_mistakes(self):
        def where_tail(way_list):

            def head_area():
                def add_dots_left_right(way, x, y):
                    for j in range(12):
                        way.add((x, y + j))

                def add_dots_up_down(way, x, y):
                    for k in range(12):
                        way.add((x + k, y))

                left, right, up, down = set(), set(), set(), set()
                for b in range(4):
                    add_dots_left_right(left, self.snake.x1-b, self.snake.y1-b)
                    add_dots_left_right(right, self.snake.x1+10+b, self.snake.y1-b)
                    add_dots_up_down(up, self.snake.x1-b, self.snake.y1-b)
                    add_dots_up_down(down, self.snake.x1-b, self.snake.y1+10+b)
                self.test.update(left, right, up, down)
                head_dict = {'left': left,
                             'right': right,
                             'up': up,
                             'down': down,
                             }
                return head_dict

            if self.flag_tail:
                for i in way_list:
                    if len(head_area()[i].intersection(self.snake.snake_body_dots)) != 0:
                        way_list.remove(i)
            return way_list

        # Перевірка шляхів куди можна іти(не назад та не на хвіст)
        try:
            if (self.snake.block_list[-1][0] + 1, self.snake.block_list[-1][1]) == self.snake.block_list[-2]:
                return where_tail(['left', 'down', 'up'])
            elif (self.snake.block_list[-1][0] - 1, self.snake.block_list[-1][1]) == self.snake.block_list[-2]:
                return where_tail(['right', 'up', 'down'])
            elif (self.snake.block_list[-1][0], self.snake.block_list[-1][1] + 1) == self.snake.block_list[-2]:
                return where_tail(['left', 'up', 'right'])
            elif (self.snake.block_list[-1][0], self.snake.block_list[-1][1] - 1) == self.snake.block_list[-2]:
                return where_tail(['right', 'down', 'left'])
            else:
                return where_tail(['right', 'down', 'left', 'up'])
        except IndexError:
            return where_tail(['right', 'down', 'left', 'up'])

    # Правильний шлях
    def true_going(self):

        def true_way_chek(way):
            result_not_back = self.exceptions_mistakes()
            if way in result_not_back:
                self.sides[way]()
            else:
                print(result_not_back[random.randint(0, len(result_not_back) - 1)])
                self.sides[result_not_back[random.randint(0, len(result_not_back) - 1)]]()

        if self.snake.block_list[-1][0] + 5 > self.food.food_x + 5 and self.snake.block_list[-1][1] + 5 > \
                self.food.food_y + 5:
            # 'зліва зверху'
            if (self.snake.block_list[-1][0] + 5) - (self.food.food_x + 5) > (self.snake.block_list[-1][1] + 5) - (
                    self.food.food_y + 5):
                true_way_chek('left')
            else:
                true_way_chek('up')

        elif self.snake.block_list[-1][0] + 5 < self.food.food_x + 5 and self.snake.block_list[-1][
            1] + 5 > self.food.food_y + 5:
            # 'зправа зверху'
            if (self.food.food_x + 5) - (self.snake.block_list[-1][0] + 5) > (self.snake.block_list[-1][1] + 5) - (
                    self.food.food_y + 5):
                true_way_chek('right')
            else:
                true_way_chek('up')

        elif self.snake.block_list[-1][0] + 5 > self.food.food_x + 5 and self.snake.block_list[-1][
            1] + 5 < self.food.food_y + 5:
            # 'зліва знизу'
            if (self.snake.block_list[-1][0] + 5) - (self.food.food_x + 5) > (self.food.food_y + 5) - (
                    self.snake.block_list[-1][1] + 5):
                true_way_chek('left')
            else:
                true_way_chek('down')

        elif self.snake.block_list[-1][0] + 5 < self.food.food_x + 5 and self.snake.block_list[-1][
            1] + 5 < self.food.food_y + 5:
            # 'зправа знизу'
            if (self.food.food_x + 5) - (self.snake.block_list[-1][0] + 5) > (self.food.food_y + 5) - (
                    self.snake.block_list[-1][1] + 5):
                true_way_chek('right')
            else:
                true_way_chek('down')

    # Виключення наступу на хвіст
    def check_tail_on(self):
        self.flag_tail = True

    # Головний цикл гри бота
    def play(self):
        while self.flag_game:
            time.sleep(random.uniform(self.bot_frequency[0], self.bot_frequency[1]))
            self.true_going()

    # Відключення бота при закритті гри
    def end(self, flag):
        if not flag:
            self.flag_game = False
