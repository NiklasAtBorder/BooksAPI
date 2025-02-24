from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 0, "book": "The Great Gatsby", "writer": "F. Scott Fitzgerald"},
    {"id": 1, "book": "The Lord of the Rings", "writer": "J. R. R. Tolkien"},
    {"id": 2, "book": "Adventures of Huckleberry Finn", "writer": "Mark Twain"},
]

@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    return books[book_id]

@app.get("/books")
def get_books(writer: str = ""):
    if writer != "":
        return [n for n in books if n["writer"] == writer]
    return books    

