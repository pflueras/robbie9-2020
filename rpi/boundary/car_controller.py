import time

from flask import Flask, jsonify

from car.car import Car
from service.image_analysis import ImageAnalysisService


class CarController:
    def __init__(self, car: Car, flask_app: Flask, image_analysis_service: ImageAnalysisService):
        self._car = car
        self._flaskApp = flask_app
        self._imageAnalysisService = image_analysis_service
        self._flaskApp.route("/status", methods=['GET'])(self.status)
        self._flaskApp.route("/run", methods=['PUT'])(self.run)

    def status(self):
        return jsonify(status=str(self._car.status.name))

    def run(self):
        for i in range(5):
            image_taken = 'img_' + str(i) + '.png'
            self._car.take_picture(image_taken)
            self._imageAnalysisService.upload_image(image_taken)
            self._imageAnalysisService.detect_traffic_light(image_taken)
            self._car.move_forward()
            time.sleep(1)

        return self.status()
