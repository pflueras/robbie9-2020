import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import * as io from 'socket.io-client';
import { CarStatus, EventModel } from './car.model';

@Injectable({
  providedIn: 'root',
})
export class CarService {
  socket: SocketIOClient.Socket;
  events: EventModel[] = [];

  constructor(private http: HttpClient) {}

  connect(): void {
    console.log('CarService => connect');
    const socket = io.connect('http://localhost:5000');
    this.socket = socket;

    socket.on('connect', () => {
      console.log('SCOKET => connect');
      socket.send('Client connected');
    });

    socket.on(CarStatus.TAKING_IMAGE, (data) => {
      console.log('SOCKET =>', CarStatus.TAKING_IMAGE);
      const event: EventModel = {
        type: CarStatus.TAKING_IMAGE,
        data: data,
      };
      this.events.push(event);
    });

    socket.on(CarStatus.IMAGE_TAKEN, (data) => {
      console.log('SOCKET =>', CarStatus.IMAGE_TAKEN);
      const event: EventModel = {
        type: CarStatus.IMAGE_TAKEN,
        data: data,
      };
      this.events.push(event);
    });
  }

  start() {
    console.log('CarService => startCar');
    this.http.put('http://localhost:5000/run', {}).subscribe();
  }

  stop() {
    console.log('CarService => stopCar');
    this.http.post('http://localhost:5000/stop', {}).subscribe();
  }

  disconnect() {
    console.log('CarService => disconnect');
    this.socket.disconnect();
  }
}
