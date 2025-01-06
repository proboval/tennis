class Field:
    h = int()
    w = int()

    def __init__(self):
        h = 64
        w = 16


class Racket:
    l = int()

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
    complexity = int()
    field = Field()
    lRacket = Racket()
    rRacket = Racket()
