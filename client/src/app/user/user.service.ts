import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface User {
  avatar: string;
  email: string;
  first_name: string;
  id: number;
  last_name: string;
}

interface UserResponse {
  data: User[];
  page: number;
  total: number;
}

@Injectable()
export class UserService {
  constructor(private http: HttpClient) {}

  get() {
    return this.http.get<UserResponse>('https://reqres.in/api/users?delay=2');
  }
}
