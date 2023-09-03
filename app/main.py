import strawberry

from app.resolver import users as users_resolver
from app.schema import users as users_schema

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
  users: list[users_schema.Users] = strawberry.field(resolver= users_resolver.get_all_users)

schema = strawberry.Schema(query=Query)