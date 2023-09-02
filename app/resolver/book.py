from app.schema import schema
from app.data.dto import books as BooksDto

def get_all_books() -> schema.Book:
    return BooksDto.BookDto.get_dto_all_books()