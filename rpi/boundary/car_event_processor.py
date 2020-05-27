from pydispatch import dispatcher

from car.car_status import CarStatus


class CarEventProcessor:
    def __init__(self, socketio):
        dispatcher.connect(self.running, signal=CarStatus.RUNNING, sender=dispatcher.Any)

        dispatcher.connect(self.stopped, signal=CarStatus.STOPPED, sender=dispatcher.Any)

        dispatcher.connect(self.take_picture, signal=CarStatus.TAKE_PICTURE, sender=dispatcher.Any)

        dispatcher.connect(self.uploading_image, signal=CarStatus.UPLOADING_IMAGE, sender=dispatcher.Any)

        dispatcher.connect(self.image_uploaded, signal=CarStatus.IMAGE_UPLOADED, sender=dispatcher.Any)

        dispatcher.connect(self.analyse_image, signal=CarStatus.ANALYSE_IMAGE, sender=dispatcher.Any)

        dispatcher.connect(self.traffic_light_detected, signal=CarStatus.TRAFFIC_LIGHT_DETECTED, sender=dispatcher.Any)

        dispatcher.connect(self.traffic_light_not_present, signal=CarStatus.TRAFFIC_LIGHT_NOT_PRESENT,
                           sender=dispatcher.Any)

        dispatcher.connect(self.move_forward, signal=CarStatus.MOVE_FORWARD, sender=dispatcher.Any)

        self._socketio = socketio

    def take_picture(self):
        self._socketio.emit('take_picture', 'took picture', broadcast=True)
        print('took picture')

    def uploading_image(self):
        self._socketio.emit('uploading_image', 'uploaded image', broadcast=True)
        print('uploaded image')

    def traffic_light_detected(self):
        self._socketio.emit('traffic_light_detected', 'detected traffic light', broadcast=True)
        print('detected traffic light')

    def traffic_light_not_present(self):
        self._socketio.emit('traffic_light_not_present', 'traffic light not detected', broadcast=True)
        print('traffic light not detected')

    def move_forward(self):
        self._socketio.emit('move_forward', 'moving forward', broadcast=True)
        print('moving forward')

    def running(self):
        self._socketio.emit('running', 'running', broadcast=True)
        print('running')

    def stopped(self):
        self._socketio.emit('stopped', 'stopped', broadcast=True)
        print('stopped')

    def image_uploaded(self):
        self._socketio.emit('image_uploaded', 'image uploaded', broadcast=True)
        print('image uploaded')

    def analyse_image(self):
        self._socketio.emit('analyse_image', 'image analise', broadcast=True)
        print('image analise')
