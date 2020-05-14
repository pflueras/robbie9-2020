import time
from threading import Thread

from car.car import Car
from service.image_analysis import ImageAnalysisService
from boundary.car_event_processor import CarEventProcessor


class CarThread(Thread):
    def __init__(self, car: Car, image_analysis_service: ImageAnalysisService, car_event_processor: CarEventProcessor):
        super(CarThread, self).__init__()
        self._car: Car = car
        self._imageAnalysisService: ImageAnalysisService = image_analysis_service
        self._running = True
        self.car_event_processor = car_event_processor

    def run(self) -> None:
        while self._running:
            image_taken = 'img.png'
            self.car_event_processor.change_status("Car is running.. ", self._car.status)
            self._car.take_picture(image_taken, self.car_event_processor)
            self._imageAnalysisService.upload_image(image_taken)
            self._imageAnalysisService.detect_traffic_light(image_taken)
            self._car.move_forward()
            time.sleep(1)
        self._car.stop()

    def stop(self):
        self._running = False
