import random
import time


class Bot:
    def __init__(self):
        self.complexity = 70
        self.flag_game = True
        self.bot_frequency = (0.5, 4)

    def play(self):
        while self.flag_game:
            time.sleep(random.uniform(self.bot_frequency[0], self.bot_frequency[1]))
            print('Hello I`m Bot, How are you?')

    def end(self, flag):
        if not flag:
            self.flag_game = False