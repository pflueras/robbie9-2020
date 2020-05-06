from car.car import Car
from enum import Enum

class CarStatus(Enum):
    STOPPED=1
    RUNNING=2

    print(CarStatus.RUNNING)
    print(CarStatus(1))

    for Status in CarStatus:
        print(Status)