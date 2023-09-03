
import datetime
import strawberry

@strawberry.type(name="Users")
class Users:
  id: strawberry.ID
  first_name: str
  last_name: str
  first_name_kana: str
  last_name_kana: str
  age: int
  gender: int
  created_at: datetime.datetime
  updated_at: datetime.datetime