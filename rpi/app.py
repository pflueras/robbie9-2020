import jsonify as jsonify
from flask import Flask
from car.car import Car

from rpi.boundary.car_controller import CarController

app = Flask(__name__)


@app.route('/')
def index():
    return 'index.html'


@app.route('/status', methods=['GET'])
def state():
    return jsonify([car.status])


if __name__ == '__main__':
    car = Car(17, 18, 22, 23, 5, 6, 12, 13, 1920, 1080, 270)
    controller = CarController(car)
    controller.run()
