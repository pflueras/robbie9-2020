from pydispatch import dispatcher
from flask_socketio import SocketIO, send

from car.car_status import CarStatus


class CarEventProcessor:
    def __init__(self, socketio: SocketIO):
        dispatcher.connect(self.running, signal=CarStatus.RUNNING, sender=dispatcher.Any)

        dispatcher.connect(self.stopped, signal=CarStatus.STOPPED, sender=dispatcher.Any)

        dispatcher.connect(self.take_picture, signal=CarStatus.TAKE_PICTURE, sender=dispatcher.Any)

        dispatcher.connect(self.uploading_image, signal=CarStatus.UPLOADING_IMAGE, sender=dispatcher.Any)

        dispatcher.connect(self.image_uploaded, signal=CarStatus.IMAGE_UPLOADED, sender=dispatcher.Any)

        dispatcher.connect(self.analyse_image, signal=CarStatus.ANALYSE_IMAGE, sender=dispatcher.Any)

        dispatcher.connect(self.traffic_light_detected, signal=CarStatus.TRAFFIC_LIGHT_DETECTED, sender=dispatcher.Any)

        dispatcher.connect(self.traffic_light_not_present, signal=CarStatus.TRAFFIC_LIGHT_NOT_PRESENT, sender=dispatcher.Any)

        dispatcher.connect(self.move_forward, signal=CarStatus.MOVE_FORWARD, sender=dispatcher.Any)

        self._socketio = socketio

    def take_picture(self):
        self._socketio.emit('take_picture', 'took picture')
        print('took picture')

    def uploading_image(self):
        self._socketio.emit('uploading_image', 'uploaded image')
        print('uploaded image')

    def traffic_light_detected(self):
        self._socketio.emit('traffic_light_detected', 'detected traffic light')
        print('detected traffic light')

    def traffic_light_not_present(self):
        self._socketio.emit('traffic_light_not_present', 'traffic light not detected')
        print('traffic light not detected')

    def move_forward(self):
        self._socketio.emit('move_forward', 'moving forward')
        print('moving forward')

    def running(self):
        self._socketio.emit('running', 'running')
        print('running')

    def stopped(self):
        self._socketio.emit('stopped', 'stopped')
        print('stopped')

    def image_uploaded(self):
        self._socketio.emit('image_uploaded', 'image uploaded')
        print('image uploaded')

    def analyse_image(self):
        self._socketio.emit('analyse_image', 'image analise')
        print('image analise')