import time
from car.car import Car

if __name__ == '__main__':
    car = Car(17, 18, 22, 23, 5, 6, 12, 13, 1920, 1080, 270)

    for i in range(5):
        car.move_forward()
        car.stop()
        car.take_picture('img_' + str(i) + '.png')
        time.sleep(1)
