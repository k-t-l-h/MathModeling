import random
import sys

class LCKM:
    # константы генератора
    # ПОДОБРАТЬ КОНСТАНТЫ
    a = 23
    c = 48
    m = 433

    # длина массива
    n = 625

    # индекс числа
    index = 0

    LC = []

    def __init__(self):
        self.LC = [0] * self.n

        self.LC[0] = random.randint(0, sys.maxsize) % self.m

        for i in range(1, self.n):
            self.LC[i] = (self.a * self.LC[i-1] + self.c) % self.m

    def get_number(self):
        self.index = self.index + 1 % self.n
        return self.LC[self.index]