from fastapi import HTTPException, status
from .book_bases import BookIn, BookDb
from sqlmodel import Session, select


def create_book(session: Session,book_in: BookIn):
    b = BookDb.model_validate(book_in)
    session.add(b)
    session.commit()
    session.refresh(b)
    return b

def get_books(session: Session, writer: str = ""):
    if writer != "":
        return session.exec(select(BookDb).where(BookDb.writer == writer)).all()
    return session.exec(select(BookDb)).all()

def get_book_by_id(session: Session, book_id: int):
    b = session.get(BookDb, book_id)
    if not b:
        raise HTTPException(
            detail=f"Book {book_id} not found.", status_code=status.HTTP_404_NOT_FOUND
        )
    return b
    
def delete_book(session: Session, book_id: int):
    b = session.get(BookDb, book_id)
    if not b:
        raise HTTPException(
            detail=f"Book {book_id} not found.", status_code=status.HTTP_404_NOT_FOUND
        )
    return {"message": f"book {book_id} deleted"}
