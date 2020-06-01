import time
from threading import Thread
from car.car import Car
from pydispatch import dispatcher
from car.car_status import CarStatus
from service.image_analysis import ImageAnalysisService
from service.events import Image, S3Image, TrafficLight

image_uri_folder: str = '/static/images/'


class CarThread(Thread):
    def __init__(self, car: Car, image_analysis_service: ImageAnalysisService):
        super(CarThread, self).__init__()
        self._car: Car = car
        self._imageAnalysisService: ImageAnalysisService = image_analysis_service
        self._running = False

    def run(self) -> None:
        max_iterations: int = 10
        current_iteration: int = 0

        self._running = True
        while self._running and current_iteration < max_iterations:
            image_filename: str = 'img_' + str(current_iteration) + ".png"

            self.take_picture(image_filename)
            if not self._running:
                print('Received stop request!')
                break

            self.upload_image(image_filename)
            if not self._running:
                print('Received stop request!')
                break

            if self.analyse_image(image_filename):
                # reached traffic light: stop!
                break
            if not self._running:
                print('Received stop request!')
                break

            self.forward_car()
            if not self._running:
                print('Received stop request!')
                break

            current_iteration += 1
        self._running = False

    def take_picture(self, image_filename):
        dispatcher.send(signal=CarStatus.TAKING_IMAGE, sender=self)
        self._car.take_picture(image_filename)
        dispatcher.send(signal=CarStatus.IMAGE_TAKEN, sender=self, message=Image(image_uri_folder + image_filename))

    def upload_image(self, image_filename):
        dispatcher.send(signal=CarStatus.UPLOADING_IMAGE, sender=self)
        self._car.status = CarStatus.TAKING_IMAGE
        s3_image_url = self._imageAnalysisService.upload_image(image_filename)
        self._car.status = CarStatus.IMAGE_TAKEN
        dispatcher.send(signal=CarStatus.IMAGE_UPLOADED, sender=dispatcher.Any,
                        message=S3Image(s3_image_url, image_uri_folder + image_filename))

    def analyse_image(self, image_filename) -> bool:
        dispatcher.send(signal=CarStatus.ANALYSING_IMAGE)
        self._car.status = CarStatus.ANALYSING_IMAGE
        analysis_result = self._imageAnalysisService.detect_traffic_light(image_filename)
        if analysis_result[0]:
            dispatcher.send(signal=CarStatus.TRAFFIC_LIGHT_DETECTED, sender=dispatcher.Any,
                            message=TrafficLight(analysis_result[1], analysis_result[2], analysis_result[3]))
            self._car.status = CarStatus.TRAFFIC_LIGHT_DETECTED
            return True
        else:
            dispatcher.send(signal=CarStatus.TRAFFIC_LIGHT_NOT_PRESENT, sender=dispatcher.Any)
            self._car.status = CarStatus.TRAFFIC_LIGHT_NOT_PRESENT
            return False

    def forward_car(self):
        dispatcher.send(signal=CarStatus.MOVING_FORWARD, sender=dispatcher.Any)
        self._car.move_forward()
        time.sleep(1)
        self._car.stop()
        dispatcher.send(signal=CarStatus.STOPPED, sender=dispatcher.Any)

    def stop(self):
        self._running = False

    @property
    def running(self):
        return self._running
