from pydispatch import dispatcher

from car.car import Car

class CarEventProcessor:
    def __init__(self, car: Car):
        self._car = car
        dispatcher.connect(self.change_status, signal=self._car.status, sender=self._car)

    def change_status(self, message, car_status):
        print(message)
        print("Status has changed: ", car_status)
        dispatcher.send(self._car, self._car.status)
