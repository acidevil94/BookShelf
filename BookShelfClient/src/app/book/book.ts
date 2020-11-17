export class Book {

    readonly bookID: number;
    readonly bookName: string;


    constructor(bookId: number, bookName: string) {
        this.bookID = bookId;
        this.bookName = bookName;
    }


    static buildEmptyBook(): Book {
        return new Book(0, "");
    }


    static fromREST(book:any) : Book{
        return new Book(book.book_id, book.book_name);
    }


    static buildObjectForREST(id:number, name:string) {
        return {
            book_id: id,
            book_name: name
        };
    }
}