import random
import sys

class MersenneTwister:
    mask = int('0bFFFFFFFF', 16)  # маска для 32-битного числа
    mask32th = int('0b990B0DF', 16)  # маска для старшего бита
    mask31th = int('0b7FFFFFFF', 16)  # маска для оставшихся 31 битов
    index = 0
    n = 624  # количество плоскостей
    magic = 623  # магическая константа для генерации
    # 32-битные константы
    A = int('0b9908B000DF', 16)
    B = int('0b9D2C568016', 16)
    C = int('0bEFC6000016', 16)

    m = 397  # сдвиг
    r = 31
    l = 18
    u = 11
    s = 7
    t = 15

    MT = []

    # заполнение вектора
    def __init__(self):
        self.MT = [0] * self.n
        seed = self.mask & random.randint(0, sys.maxsize)
        self.MT[0] = seed

        for i in range(1, self.n):
            self.MT[i] = (self.magic * (self.MT[i - 1] ^ (self.MT[i - 1] >> 30))) + i
        self.__twister__()

    # закалка вектора
    def __twister__(self):
        for i in range(self.n):
            tmp = ((self.MT[i] & self.mask32th) + (self.MT[(i + 1) % self.n]) & self.mask31th)
            self.MT[i] = (self.MT[(i + 1) % self.n] ^ (tmp >> 1)) & self.mask
            if tmp % 2 == 1:
                self.MT[i] = self.MT[i] ^ self.A

    def get_number(self):
        if self.index == 0:
            self.__init__()

        x = self.MT[self.index]
        x = x ^ (x >> self.u)
        x = x ^ (x << self.s) & self.B
        x = x ^ (x << self.t) & self.C
        x = x ^ (x << self.l)

        self.index = (self.index + 1) % self.n

        return x