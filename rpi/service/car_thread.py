import time
from threading import Thread
from car.car import Car
from pydispatch import dispatcher
from car.car_status import CarStatus
from service.image_analysis import ImageAnalysisService

class CarThread(Thread):
    def __init__(self, car: Car, image_analysis_service: ImageAnalysisService):
        super(CarThread, self).__init__()
        self._car: Car = car
        self._imageAnalysisService: ImageAnalysisService = image_analysis_service
        self._running = True

    def run(self) -> None:
        while self._running:
            image_taken = 'img.png'

            self._car.take_picture(image_taken)
            dispatcher.send(signal=CarStatus.TAKE_PICTURE, sender=dispatcher.Any)

            self._imageAnalysisService.upload_image(image_taken)
            dispatcher.send(signal=CarStatus.UPLOADING_IMAGE, sender=dispatcher.Any)

            if (self._imageAnalysisService.detect_traffic_light(image_taken)):
                dispatcher.send(signal=CarStatus.TRAFFIC_LIGHT_DETECTED, sender=dispatcher.Any)
            else:
                dispatcher.send(signal=CarStatus.TRAFFIC_LIGHT_NOT_PRESENT, sender=dispatcher.Any)

            self._car.move_forward()
            dispatcher.send(signal=CarStatus.MOVE_FORWARD, sender=dispatcher.Any)

            time.sleep(1)

        self._car.stop()
        dispatcher.send(signal=CarStatus.STOPPED, sender=dispatcher.Any)

    def stop(self):
        self._running = False
