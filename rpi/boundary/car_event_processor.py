from pydispatch import dispatcher
from car.car_status import CarStatus
from service.events import Image, S3Image, TrafficLight


class CarEventProcessor:
    def __init__(self, flask_app, socket_io):
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

        self._flaskApp = flask_app
        self._socketIo = socket_io

    def taking_image(self):
        print('[' + type(self).__name__ + '] taking image...')
        with self._flaskApp.test_request_context():
            self._socketIo.emit(CarStatus.TAKING_IMAGE.name, '', broadcast=True)

    def image_taken(self, message: Image):
        print('[' + type(self).__name__ + '] image taken: ' + message.image_uri)
        with self._flaskApp.test_request_context():
            self._socketIo.emit(CarStatus.IMAGE_TAKEN.name, message.properties, broadcast=True)

    def uploading_image(self):
        print('[' + type(self).__name__ + '] uploading image...')
        with self._flaskApp.test_request_context():
            self._socketIo.emit(CarStatus.IMAGE_UPLOADED.name, '', broadcast=True)

    def image_uploaded(self, message: S3Image):
        print('[' + type(self).__name__ + '] image uploaded: ' + message.s3_image_url)
        with self._flaskApp.test_request_context():
            self._socketIo.emit(CarStatus.IMAGE_UPLOADED.name, message.properties, broadcast=True)

    def analysing_image(self):
        print('[' + type(self).__name__ + '] analysing image...')
        with self._flaskApp.test_request_context():
            self._socketIo.emit(CarStatus.ANALYSING_IMAGE.name, '', broadcast=True)

    def traffic_light_not_present(self):
        print('[' + type(self).__name__ + '] traffic light not detected!')
        with self._flaskApp.test_request_context():
            self._socketIo.emit(CarStatus.TRAFFIC_LIGHT_NOT_PRESENT.name, '', broadcast=True)

    def traffic_light_detected(self, message: TrafficLight):
        print('[' + type(self).__name__ + '] traffic light detected! Accuracy : ' + message.accuracy)
        with self._flaskApp.test_request_context():
            self._socketIo.emit(CarStatus.TRAFFIC_LIGHT_DETECTED.name, message.properties, broadcast=True)

    def move_forward(self):
        print('[' + type(self).__name__ + '] moving the car forward...')
        with self._flaskApp.test_request_context():
            self._socketIo.emit(CarStatus.MOVING_FORWARD.name, '', broadcast=True)

    def stopped(self):
        print('[' + type(self).__name__ + '] car stopped!')
        with self._flaskApp.test_request_context():
            self._socketIo.emit(CarStatus.STOPPED.name, '', broadcast=True)
