import strawberry

from app.resolver import books as resolverBook
from app.schema import books as schemaBooks

# Query Example
# @strawberry.type
# class Query:
#     task: TaskType = strawberry.field(resolver=get_task)
#     tasks: list[TaskType] = strawberry.field(resolver=get_tasks)


# Mutation Example
# @strawberry.type
# class Mutation:
#     task_add: TaskType = strawberry.field(resolver=add_task)
#     task_update: TaskType = strawberry.field(resolver=update_task)
#     task_delete: TaskType = strawberry.field(resolver=delete_task)


# schema = strawberry.Schema(query=Query, mutation=Mutation)

@strawberry.type
class Query:
    book: list[schemaBooks.Book] = strawberry.field(resolver= resolverBook.get_all_books)

books = strawberry.Schema(query=Query)