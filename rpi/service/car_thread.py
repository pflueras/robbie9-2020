import time
from threading import Thread
from car.car import Car
from pydispatch import dispatcher
from service.image_analysis import ImageAnalysisService
from shared import status_signals

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
            dispatcher.send(message='taking image',
                            signal=status_signals.TAKE_PICTURE_SIGNAL,
                            sender=status_signals.TAKE_PICTURE_SENDER)

            self._imageAnalysisService.upload_image(image_taken)
            dispatcher.send(message='uploading image',
                            signal=status_signals.UPLOAD_IMAGE_SIGNAL,
                            sender=status_signals.UPLOAD_IMAGE_SENDER)

            if (self._imageAnalysisService.detect_traffic_light(image_taken)):
                dispatcher.send(message='traffic light detected',
                                signal=status_signals.TRAFFIC_LIGHT_DETECTED_SIGNAL,
                                sender=status_signals.TRAFFIC_LIGHT_DETECTED_SENDER)
            else:
                dispatcher.send(message='traffic light not detected',
                                signal=status_signals.TRAFFIC_LIGHT_NOT_PRESENT_SIGNAL,
                                sender=status_signals.TRAFFIC_LIGHT_NOT_PRESENT_SENDER)

            self._car.move_forward()
            dispatcher.send(message='moving forward',
                            signal=status_signals.MOVE_FORWARD_SIGNAL,
                            sender=status_signals.MOVE_FORWARD_SENDER)

            time.sleep(1)
        self._car.stop()

    def stop(self):
        self._running = False
