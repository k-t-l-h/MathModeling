import random
import sys

class MeanSq:

    lmask = int('0bFFFF', 16)
    rmask = 8
    n = 625  # длина

    index = 0

    MS = []

    def __init__(self):
        self.MS = [0]* self.n
        self.MS[0] = random.randint(0, sys.maxsize) & self.lmask

        for i in range(1, self.n):
            self.MS[i] = pow(self.MS[i - 1], 2) >> self.rmask & self.lmask
            if self.MS[i - 1] == 0:
                self.MS[i] = random.randint(0, sys.maxsize / 2) & self.lmask

    def get_number(self):
        self.index = self.index + 1 % self.n
        return self.MS[self.index]