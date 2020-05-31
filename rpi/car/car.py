from car.camera import Camera
from car.car_status import CarStatus
from car.motor import Motor


class Car:
    """ This car represents the Raspberry Pi car """

    def __init__(self, m1_forward, m1_backward, m2_forward, m2_backward, m3_forward, m3_backward, m4_forward,
                 m4_backward, resolution_x, resolution_y, rotation, status=CarStatus.STOPPED):
        self._camera = Camera(resolution_x, resolution_y, rotation)
        self._motor1 = Motor(m1_forward, m1_backward)
        self._motor2 = Motor(m2_forward, m2_backward)
        self._motor3 = Motor(m3_forward, m3_backward)
        self._motor4 = Motor(m4_forward, m4_backward)
        self._status = status

    def move_forward(self) -> None:
        self._status = CarStatus.MOVING_FORWARD
        self._motor1.move_forward()
        self._motor2.move_forward()
        self._motor3.move_forward()
        self._motor4.move_forward()

    def move_backward(self) -> None:
        self._status = CarStatus.MOVING_BACKWARD
        self._motor1.move_backward()
        self._motor2.move_backward()
        self._motor3.move_backward()
        self._motor4.move_backward()

    def stop(self) -> None:
        self._status = CarStatus.STOPPED
        self._motor1.stop()
        self._motor2.stop()
        self._motor3.stop()
        self._motor4.stop()

    def take_picture(self, image_filename) -> None:
        self._status = CarStatus.TAKING_IMAGE
        self._camera.take_picture(image_filename)
        self._status = CarStatus.IMAGE_TAKEN

    def update_status(self, status: CarStatus) -> None:
        self._status = status

    @property
    def status(self) -> CarStatus:
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
