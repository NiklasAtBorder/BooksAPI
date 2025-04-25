from fastapi import HTTPException, status
from .book_bases import BookIn, BookDb

books = [
    {"id": 0, "book": "The Great Gatsby", "writer": "F. Scott Fitzgerald"},
    {"id": 1, "book": "The Lord of the Rings", "writer": "J. R. R. Tolkien"},
    {"id": 2, "book": "Adventures of Huckleberry Finn", "writer": "Mark Twain"},
]

def create_book(book_in: BookIn):
    new_id = len(books)
    book = BookDb(**book_in.model_dump(), id=new_id)
    books.append(book.model_dump())
    return book

def get_books(writer: str = ""):
    if writer != "":
        return [b for b in books if b["writer"] == writer]
    return books

def get_book_by_id(book_id: int):
    b = [b for b in books if b['id'] == book_id]
    if len(b) != 0:
        return b[0]
    else:
        raise HTTPException(
            detail=f"Book {book_id} not found.", status_code=status.HTTP_404_NOT_FOUND
        )
    
def delete_book(book_id: int):
    b = [b for b in books if b['id'] == book_id]
    if len(b) != 0:
        del books[book_id]
        return {"message": f"Book {book_id} deleted."}
    else:
        raise HTTPException(
            detail=f"Book {book_id} not found.", status_code=status.HTTP_404_NOT_FOUND
        )
