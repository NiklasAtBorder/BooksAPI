from sqlmodel import SQLModel, Field


class BookBase(SQLModel):
    name: str
    writer: str

class BookIn(BookBase):
    pass

class BookDb(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)