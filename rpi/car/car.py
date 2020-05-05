from car.camera import Camera
from car.motor import Motor

from rpi.car.carStatus import CarStatus


class Car:
    # Car constructor with the definition of the required inputs
    # status variable used to determine the state of the car: RUNNING or STOPPED
    def __init__(self, m1_forward, m1_backward, m2_forward, m2_backward, m3_forward, m3_backward, m4_forward,
                 m4_backward, resolution_x, resolution_y, rotation, status=CarStatus.STOPPED):
        self._camera = Camera(resolution_x, resolution_y, rotation)
        self._motor1 = Motor(m1_forward, m1_backward)
        self._motor2 = Motor(m2_forward, m2_backward)
        self._motor3 = Motor(m3_forward, m3_backward)
        self._motor4 = Motor(m4_forward, m4_backward)
        self.status = status

    # moving forward method
    def move_forward(self):
        self.status = CarStatus.RUNNING
        print('Moving the car forward...')
        self._motor1.move_forward()
        self._motor2.move_forward()
        self._motor3.move_forward()
        self._motor4.move_forward()

    # moving backwards method
    def move_backward(self):
        self.status = CarStatus.RUNNING
        print('Moving the car backward...')
        self._motor1.move_backward()
        self._motor2.move_backward()
        self._motor3.move_backward()
        self._motor4.move_backward()

    # stopping method
    def stop(self):
        self.status = CarStatus.RUNNING
        print('Stopping the car...')
        self._motor1.stop()
        self._motor2.stop()
        self._motor3.stop()
        self._motor4.stop()

    # taking picture method
    def take_picture(self, image_filename):
        self._camera.take_picture(image_filename)
