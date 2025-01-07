
class Ball:
    _x: int
    _y: int
    _h_speed: int
    _w_speed: int

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def change_position(self):
        self._y += self._h_speed
        self._x += self._w_speed

    def change_w_speed(self):
        self._w_speed *= -1

    def change_h_speed(self):
        self._h_speed *= -1

    def add_d_h_speed(self, d):
        self._h_speed += d