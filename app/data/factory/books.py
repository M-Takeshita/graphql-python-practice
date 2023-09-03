from app.schema import books

# 
class BooksFactory: 
  def get_dto_all_books():
    return [
      books.Book(
          id= 1,
          title="The Great Gatsby",
          description="hello world",
      ),
    ]