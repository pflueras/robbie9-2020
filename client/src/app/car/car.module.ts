import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CarRoutingModule } from './car-routing.module';
import { CarPageComponent } from './car-page.component';

@NgModule({
  declarations: [CarPageComponent],
  imports: [CommonModule, CarRoutingModule],
})
export class CarModule {}
