from app.schema import schema

class BookDto: 
  def get_dto_all_books():
    return [
      schema.Book(
          id= 1,
          title="The Great Gatsby",
          description="hello world",
      ),
    ]