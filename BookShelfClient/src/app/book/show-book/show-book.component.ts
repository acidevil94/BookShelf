import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

import {Book} from '../book';

@Component({
  selector: 'app-show-book',
  templateUrl: './show-book.component.html',
  styleUrls: ['./show-book.component.css']
})
export class ShowBookComponent implements OnInit {

  constructor(private service: SharedService) { }

  BookList: Array<Book>=[];

  ModalTitle: string ="";
  ActivateAddEditBookComponent:boolean = false;
  MyBook: Book ;

  ngOnInit(): void {
    this.refreshBookList();
  }

  addBookClick() {
    this.MyBook = Book.buildEmptyBook();
    this.ModalTitle = "Add Book";
    this.ActivateAddEditBookComponent = true;
  }


  editBookClick(book:any) {
    this.MyBook = book;
    this.ModalTitle = "Edit Book";
    this.ActivateAddEditBookComponent = true;
  }

  

  closeModalClick() {
    this.ActivateAddEditBookComponent = false;
    this.refreshBookList();
  }

  refreshBookList() {
    this.service.getBookList().subscribe(data => {
      this.BookList = data;
    });
  }
}
