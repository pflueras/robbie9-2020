from datetime import datetime


class Event:
    def __init__(self):
        self._timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


class Image(Event):
    def __init__(self, image_uri: str):
        super().__init__()
        self._image_uri = image_uri

    @property
    def image_uri(self):
        return self._image_uri


class S3Image(Event):
    def __init__(self, s3_image_url: str, image_uri: str):
        super().__init__()
        self._s3_image_url = s3_image_url
        self._image_uri = image_uri

    @property
    def s3_image_url(self):
        return self._s3_image_url


class TrafficLight(Event):
    def __init__(self, point_a: tuple, point_b: tuple, accuracy: int):
        super().__init__()
        self._pointA = point_a
        self._pointB = point_b
        self._accuracy = accuracy

    @property
    def accuracy(self):
        return self._accuracy
