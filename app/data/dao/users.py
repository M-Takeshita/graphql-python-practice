from sqlalchemy.orm import scoped_session

from app.data.dao.model import users as users_model

def get_all_users(session: scoped_session[any]):
  val = session.query(users_model.Users).all()
  print(val)
  return val