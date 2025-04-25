from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    writer: str

class BookIn(BookBase):
    pass

class BookDb(BookBase):
    id: int