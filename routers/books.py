from fastapi import APIRouter, status, Depends
from ..db.book_bases import BookDb, BookIn
from ..db import books_crud
from ..db.database import get_session
from sqlmodel import Session

router = APIRouter()

@router.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book_in: BookIn, session: Session = Depends(get_session)):
    return books_crud.create_book(session, book_in)

@router.get("/books", response_model=list[BookDb])
def get_books(writer: str = "", session: Session = Depends(get_session)):
    return books_crud.get_books(session, writer)

@router.get("/books/{book_id}", response_model=BookDb)
def get_book_by_id(book_id: int, session: Session = Depends(get_session)):
    return books_crud.get_book_by_id(session, book_id)
    
@router.delete("/books/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    return books_crud.delete_book(session, book_id)