from typing import List
import os


class Field:
    h = int()
    w = int()
    f = List[List[str]]

    def __str__(self):
        s = ''
        for i in range(self.h):
            for j in range(self.w):
                s += self.f[i][j]
            s += '\n'

        return s

    def __init__(self):
        self.h = 16
        self.w = 64
        self.f = [
            ["#" if i == 0 or i == self.h - 1 or j == 0 or j == self.w - 1 else " " for j in range(self.w)]
            for i in range(self.h)
        ]


class Racket:
    l = int()
    x = int()
    y = int()

    def __init__(self):
        self.l = 2

    def set_complexity(self, complexity):
        self.l *= 4 - complexity


class Ball:
    size = int()
    speed = float()

    def __init__(self):
        self.size = 2
        self.speed = 0.5


class Game:
    _left_score = int()
    _right_score = int()
    _complexity = 1

    def __init__(self):
        self._field = Field()
        self._lRacket = Racket()
        self._rRacket = Racket()
        self._lRacket.x = 4
        self._rRacket.x = self._field.w - 5
        self._left_score = 0
        self._right_score = 0

    def start(self) -> int:
        print('Выберите сложность:\n'
              '1 - Легко\n'
              '2 - Нормально\n'
              '3 - Сложно\n')

        c = input()
        try:
            self._complexity = int(c)
            if self._complexity < 1 or self._complexity > 3:
                print('Введите одну цифру!')
                return -1
            else:
                return 1
        except:
            print('Введите одну цифру!')
            return -1

    def set_length(self):
        self._rRacket.set_complexity(self._complexity)
        self._lRacket.set_complexity(self._complexity)

    def start_game(self):
        self._rRacket.y = self._lRacket.y = self._field.h // 2 - (self._lRacket.l // 2)

        for i in range(self._lRacket.l):
            self._field.f[self._lRacket.y + i][self._lRacket.x] = '|'

        for i in range(self._rRacket.l):
            self._field.f[self._rRacket.y + i][self._rRacket.x] = '|'

        print(self._field)
