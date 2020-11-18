import { Component, OnInit, Input } from '@angular/core';

import { SharedService } from 'src/app/shared.service';

import { Book } from 'src/app/book/book';

@Component({
  selector: 'app-add-edit-book',
  templateUrl: './add-edit-book.component.html',
  styleUrls: ['./add-edit-book.component.css']
})
export class AddEditBookComponent implements OnInit {

  constructor(private service: SharedService) { }

  @Input() book:Book ;
  BookName: string = "";
  BookId:number = 0;

  ngOnInit(): void {
    this.BookId = this.book.bookID;
    this.BookName = this.book.bookName;
  }


  addClick(){
    var val = Book.buildObjectForREST(this.BookId, this.BookName);
    this.service.addBook(val).subscribe(res => {
      alert(res.toString());
    });
  }

  updateClick() {
    var val = Book.buildObjectForREST(this.BookId, this.BookName);
    this.service.updateBook(val).subscribe(res => {
      alert(res.toString());
    });
  }

}
