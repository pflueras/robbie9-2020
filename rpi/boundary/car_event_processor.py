from pydispatch import dispatcher

from car.car_status import CarStatus


class CarEventProcessor:
    def __init__(self):
        dispatcher.connect(self.running, signal=CarStatus.RUNNING, sender=dispatcher.Any)

        dispatcher.connect(self.stopped, signal=CarStatus.STOPPED, sender=dispatcher.Any)

        dispatcher.connect(self.take_picture, signal=CarStatus.TAKE_PICTURE, sender=dispatcher.Any)

        dispatcher.connect(self.uploading_image, signal=CarStatus.UPLOADING_IMAGE, sender=dispatcher.Any)

        dispatcher.connect(self.image_uploaded, signal=CarStatus.IMAGE_UPLOADED, sender=dispatcher.Any)

        dispatcher.connect(self.analyse_image, signal=CarStatus.ANALYSE_IMAGE, sender=dispatcher.Any)

        dispatcher.connect(self.traffic_light_detected, signal=CarStatus.TRAFFIC_LIGHT_DETECTED, sender=dispatcher.Any)

        dispatcher.connect(self.traffic_light_not_present, signal=CarStatus.TRAFFIC_LIGHT_NOT_PRESENT, sender=dispatcher.Any)

        dispatcher.connect(self.move_forward, signal=CarStatus.MOVE_FORWARD, sender=dispatcher.Any)

    def take_picture(self):
        print('took picture')

    def uploading_image(self):
        print('uploaded image')

    def traffic_light_detected(self):
        print('detected traffic light')

    def traffic_light_not_present(self):
        print('traffic light not detected')

    def move_forward(self):
        print('moving forward')

    def running(self):
        print('running')

    def stopped(self):
        print('stopped')

    def image_uploaded(self):
        print('image uploaded')

    def analyse_image(self):
        print('image analize')