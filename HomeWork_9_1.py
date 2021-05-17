from itertools import cycle
from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 5), ('Yellow', 3), ('Green', 30))
    def switch(self):
        for color, duration in cycle(self.__color):
            print(f'{color} wait {duration} sec')
            sleep(duration)

trafficlight = TrafficLight()
trafficlight.switch()







