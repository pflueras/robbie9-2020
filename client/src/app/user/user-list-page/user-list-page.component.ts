import { Component, OnInit } from '@angular/core';
import { UserService, User } from '../user.service';

@Component({
  selector: 'app-user-list-page',
  templateUrl: './user-list-page.component.html',
  styleUrls: ['./user-list-page.component.css'],
  providers: [UserService],
})
export class UserListPageComponent implements OnInit {
  users: User[];
  loading = false;

  today = new Date();

  constructor(private userService: UserService) {}

  ngOnInit(): void {
    this.fetchUsers();
  }

  fetchUsers() {
    this.loading = true;

    this.userService.get().subscribe((resData) => {
      this.users = resData.data;
      this.loading = false;
    });
  }

  ngOnDestory() {
    console.log('ngOnDestory');
  }
}
