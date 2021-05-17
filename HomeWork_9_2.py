class Road:
    def __init__(self,  length, width):
        self._length = length
        self._width = width
    def figure_area(self):
        area = self._length * self._width * 25 * 5
        return area

area_road = Road(10,30)

print(area_road.figure_area(), 'т.')
