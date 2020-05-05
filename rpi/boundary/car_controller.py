from rpi.car.car import Car
import time

class CarController:
    def __init__(self, car: Car):
        self.car = car

    def run(self):
        for i in range(5):
            self.car.move_forward()
            self.car.stop()
            self.car.take_picture('img_' + str(i) + '.png')
            time.sleep(1)
