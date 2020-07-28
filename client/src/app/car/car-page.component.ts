import { Component, OnInit } from '@angular/core';
import { EventModel } from './car.model';
import { CarService } from './car.service';

@Component({
  selector: 'app-car',
  templateUrl: './car-page.component.html',
})
export class CarPageComponent implements OnInit {
  events: EventModel[] = [];

  constructor(private carService: CarService) {}

  ngOnInit(): void {
    console.log('HomePageComponent => ngOnInit');

    this.carService.connect();
    this.events = this.carService.events;
  }

  startCar() {
    console.log('HomePageComponent => startCar');

    this.carService.start();
  }

  stopCar() {
    console.log('HomePageComponent => stopCar');

    this.carService.stop();
  }

  ngOnDestroy() {
    console.log('HomePageComponent => ngOnDestroy');

    this.carService.disconnect();
  }
}
