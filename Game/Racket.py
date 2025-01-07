
class Racket:
    l: int
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.l = 2
        self.x = x
        self.y = y

    def set_complexity(self, complexity):
        self.l *= 4 - complexity