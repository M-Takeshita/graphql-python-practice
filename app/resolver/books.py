from app.schema import books
from app.data.factory import books as BooksFactory

def get_all_books() -> books.Book:
    return BooksFactory.BooksFactory.get_dto_all_books()