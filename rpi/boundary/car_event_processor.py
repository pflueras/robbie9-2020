from pydispatch import dispatcher

from car.car_status import CarStatus
from service.events import Image, S3Image, TrafficLight


class CarEventProcessor:
    def __init__(self, socket_io):
        dispatcher.connect(self.taking_image, signal=CarStatus.TAKING_IMAGE, sender=dispatcher.Any)
        dispatcher.connect(self.image_taken, signal=CarStatus.IMAGE_TAKEN, sender=dispatcher.Any)
        dispatcher.connect(self.uploading_image, signal=CarStatus.UPLOADING_IMAGE, sender=dispatcher.Any)
        dispatcher.connect(self.image_uploaded, signal=CarStatus.IMAGE_UPLOADED, sender=dispatcher.Any)
        dispatcher.connect(self.analysing_image, signal=CarStatus.ANALYSING_IMAGE, sender=dispatcher.Any)
        dispatcher.connect(self.traffic_light_detected, signal=CarStatus.TRAFFIC_LIGHT_DETECTED, sender=dispatcher.Any)
        dispatcher.connect(self.traffic_light_not_present, signal=CarStatus.TRAFFIC_LIGHT_NOT_PRESENT,
                           sender=dispatcher.Any)
        dispatcher.connect(self.move_forward, signal=CarStatus.MOVING_FORWARD, sender=dispatcher.Any)
        dispatcher.connect(self.stopped, signal=CarStatus.STOPPED, sender=dispatcher.Any)

        self._socketIo = socket_io

    def taking_image(self):
        print('[' + type(self).__name__ + '] taking image...')
        self._socketIo.emit(CarStatus.TAKING_IMAGE.name, '', broadcast=True)

    def image_taken(self, message: Image):
        print('[' + type(self).__name__ + '] image taken: ' + message.image_uri)
        self._socketIo.emit(CarStatus.IMAGE_TAKEN.name, message, broadcast=True)

    def uploading_image(self):
        print('[' + type(self).__name__ + '] uploading image...')
        self._socketIo.emit(CarStatus.IMAGE_UPLOADED.name, '', broadcast=True)

    def image_uploaded(self, message: S3Image):
        print('[' + type(self).__name__ + '] image uploaded: ' + message.s3_image_url)
        self._socketIo.emit(CarStatus.IMAGE_UPLOADED.name, message, broadcast=True)

    def analysing_image(self):
        print('[' + type(self).__name__ + '] analysing image...')
        self._socketIo.emit(CarStatus.ANALYSING_IMAGE.name, 'image analise', broadcast=True)

    def traffic_light_not_present(self):
        print('[' + type(self).__name__ + '] traffic light not detected!')
        self._socketIo.emit(CarStatus.TRAFFIC_LIGHT_NOT_PRESENT.name, '', broadcast=True)

    def traffic_light_detected(self, message: TrafficLight):
        print('[' + type(self).__name__ + '] traffic light detected! Accuracy : ' + message.accuracy)
        self._socketIo.emit(CarStatus.TRAFFIC_LIGHT_DETECTED.name, message, broadcast=True)

    def move_forward(self):
        print('[' + type(self).__name__ + '] moving the car forward...')
        self._socketIo.emit(CarStatus.MOVING_FORWARD.name, '', broadcast=True)

    def stopped(self):
        print('[' + type(self).__name__ + '] car stopped!')
        self._socketIo.emit(CarStatus.STOPPED.name, '', broadcast=True)
