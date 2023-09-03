from typing import List
from app.schema import users as users_schema
from app.data import session
import app.data.dao.users as users

def get_all_users() -> List[users_schema.Users]:
  try:
    sess = session.create_default_session()
    return users.get_all_users(sess)
  except Exception as e:
    raise e
  finally:
    sess.close()