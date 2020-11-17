import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';


import {Book} from 'src/app/book/book';

@Injectable({
  providedIn: 'root'
})
export class SharedService {

  // BookShelfAPI URL
  readonly API_URL = "http://127.0.0.1:8000";
  
  // Photo Upload URL
  readonly PHOTO_URL = "/SaveFile";

  readonly BOOK_URL = "/book/";

  constructor(private http:HttpClient) { }


  getBookList(): Observable<Book[]>{
    return this.http.get<any[]>(this.API_URL + this.BOOK_URL)
                .pipe(
                  map(books => books.map(book => Book.fromREST(book))
                  )
                );
  }


  addBook(val: any) {
    return this.http.post(this.API_URL + this.BOOK_URL, val);
  }

  updateBook(val: any) {
    return this.http.put(this.API_URL + this.BOOK_URL, val);
  }

  deleteBook(id: any) {
    return this.http.delete(this.API_URL + this.BOOK_URL + id);
  }

  uploadPhoto(val: any) {
    return this.http.post(this.API_URL + this.PHOTO_URL, val);
  }

}
