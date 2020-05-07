import time
from rpi.car.car import Car
from rpi.car.car_status import CarStatus
from flask import Flask

class CarController:
    def __init__(self, car: Car):
        self._car = car

    def run(self):
        for i in range(5):
            self._car.move_forward()
            self._car.stop()
            self._car.take_picture('img_' + str(i) + '.png')
            time.sleep(1)

    def car_status(self):
        if(CarStatus.RUNNING):
            return "Running"
        else:
            return "Stop"


