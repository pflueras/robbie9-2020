import time


class ImageAnalysisService:
    def upload_image(self, image_filename: str) -> str:
        time.sleep(0.25)
        return 'https://s3.../' + image_filename

    def detect_traffic_light(self, image_filename: str):
        time.sleep(0.25)
        return (False, )
