# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, field, x: int, y: int, movement_type: str):

        self._field = field
        self._x = x
        self._y = y
        self._movement_type = movement_type

    def _calculate_speed(self, speed):
        if self._movement_type == "fly":
            return speed * 1.2
        elif self._movement_type == "crawl":
            return speed * 0.5

    def move(self, direction, speed):
        speed = self._calculate_speed(speed)

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)