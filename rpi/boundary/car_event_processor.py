from pydispatch import dispatcher
from shared import status_signals

class CarEventProcessor:
    def __init__(self):
        dispatcher.connect(self.running_dispatcher_recieve,
                           signal=status_signals.RUNNING_SIGNAL,
                           sender=status_signals.RUNNING_SENDER)
        dispatcher.connect(self.stopped_dispatcher_recieve,
                           signal=status_signals.STOPPED_SIGNAL,
                           sender=status_signals.STOPPED_SENDER)
        dispatcher.connect(self.take_picture_dispatcher_recieve,
                           signal=status_signals.TAKE_PICTURE_SIGNAL,
                           sender=status_signals.TAKE_PICTURE_SENDER)
        dispatcher.connect(self.uploading_image_dispatcher_recieve,
                           signal=status_signals.UPLOAD_IMAGE_SIGNAL,
                           sender=status_signals.UPLOAD_IMAGE_SENDER)
        dispatcher.connect(self.image_uploaded_dispatcher_recieve,
                           signal=status_signals.IMAGE_UPLOADED_SIGNAL,
                           sender=status_signals.IMAGE_UPLOADED_SENDER)
        dispatcher.connect(self.analyze_image_dispatcher_recieve,
                           signal=status_signals.ANALYZE_IMAGE_SIGNAL,
                           sender=status_signals.ANALYZE_IMAGE_SENDER)
        dispatcher.connect(self.traffic_light_detected_dispatcher_recieve,
                           signal=status_signals.TRAFFIC_LIGHT_DETECTED_SIGNAL,
                           sender=status_signals.TRAFFIC_LIGHT_DETECTED_SENDER)
        dispatcher.connect(self.traffic_light_not_present_dispatcher_recieve,
                           signal=status_signals.TRAFFIC_LIGHT_NOT_PRESENT_SIGNAL,
                           sender=status_signals.TRAFFIC_LIGHT_NOT_PRESENT_SENDER)
        dispatcher.connect(self.move_forward_dispatcher_recieve,
                           signal=status_signals.MOVE_FORWARD_SIGNAL,
                           sender=status_signals.MOVE_FORWARD_SENDER)

    def take_picture_dispatcher_recieve(self):
        print('took picture')

    def uploading_image_dispatcher_recieve(self):
        print('uploaded image')

    def traffic_light_detected_dispatcher_recieve(self):
        print('detected traffic light')

    def traffic_light_not_present_dispatcher_recieve(self):
        print('traffic light not detected')

    def move_forward_dispatcher_recieve(self):
        print('moving forward')

    def running_dispatcher_recieve(self):
        print('running')

    def stopped_dispatcher_recieve(self):
        print('stopped')

    def image_uploaded_dispatcher_recieve(self):
        print('image uploaded')

    def analyze_image_dispatcher_recieve(self):
        print('image analize')