from flask import Flask, render_template
from flask_socketio import SocketIO

from boundary.car_controller import CarController
from boundary.car_event_processor import CarEventProcessor
from car.car import Car
from service.car_service import CarService
from service.image_analysis import ImageAnalysisService

app = Flask(__name__)
socket_io = SocketIO(app, logger=True, engineio_logger=True)


@socket_io.on('connect')
def connect():
    socket_io.send('Connection established')


@socket_io.on('message')
def handle_messages(message):
    print('Message from client: ' + message)


@socket_io.on('disconnect')
def disconnect():
    print('Client disconnected')


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    car = Car(17, 18, 22, 23, 5, 6, 12, 13, 1920, 1080, 270)
    imageAnalysisService = ImageAnalysisService()
    carService = CarService(car=car, image_analysis_service=imageAnalysisService)
    carController = CarController(car=car, car_service=carService, flask_app=app)
    car_event_processor = CarEventProcessor(socket_io)
    socket_io.run(app)
