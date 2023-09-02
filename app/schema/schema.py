import typing
import strawberry

@strawberry.type(name="Books")
class Book:
    id: strawberry.ID
    title: str
    description: str