class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self} поехала'
    def stop(self):
        return f'{self} остановилась'
    def turn_direction(self, direction):
        return f'повернула {direction}'
    def show_speed(self):
        return f'Текущая сокрость {self.speed}'

class Towncar(Car):
    def show_speed(self):
        if self.speed > 60:
            difference = self.speed - 60
            return f'Ограничение сокроксти - 60; Превышение скороксти на {difference} км/ч!!!'
        else:
            return f'Текущая сокрость {self.speed}'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            difference = self.speed - 40
            return f'Ограничение сокроксти - 60; Превышение скороксти на  {difference} км/ч!!!'
        else:
            return f'Текущая сокрость {self.speed}'

class PoliceCar(Car):
    pass

towncar = Towncar(80, 'Black', 'Mazda', None)
sportcar = SportCar(220, 'Red', 'Ferrari', None)
workcar = WorkCar(30, 'Blue', 'Pegeout', None)
policecar = PoliceCar(80, 'Special', 'LADA', True)

print(sportcar.show_speed())
print(towncar.show_speed())
print(workcar.show_speed())
print(policecar.show_speed())
print(sportcar.turn_direction('Направо'))
print(policecar.color)
print(sportcar.name)