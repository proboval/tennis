from typing import List


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