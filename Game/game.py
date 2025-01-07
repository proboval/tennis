from typing import List
import os
from Game.Ball import Ball
from Game.Field import Field
from Game.Racket import Racket


class Game:
    _left_score: int
    _right_score: int
    _complexity: int
    ball: Ball
    l_racket: Racket
    r_racket: Racket
    _field: Field

    def __init__(self):
        self._field = Field()
        self._left_score = 0
        self._right_score = 0
        self.l_racket = Racket(4, 0)
        self.r_racket = Racket(self._field.w - 5, 0)

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
        self.r_racket.set_complexity(self._complexity)
        self.l_racket.set_complexity(self._complexity)

    def start_game(self):
        self.r_racket.y = self.l_racket.y = self._field.h // 2 - (self.l_racket.l // 2)

        for i in range(self.l_racket.l):
            self._field.f[self.l_racket.y + i][self.l_racket.x] = '|'

        for i in range(self.r_racket.l):
            self._field.f[self.r_racket.y + i][self.r_racket.x] = '|'

        print(self._field)

