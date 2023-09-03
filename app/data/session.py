from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine import Engine
from app.data import engine as default_engine
 
def create_default_session():
  return scoped_session(
    sessionmaker(
      autocommit = False,
      autoflush = False,
      bind = default_engine.engine
    )
  )

def create_any_session(engine: Engine):
  return scoped_session(
    sessionmaker(
      autocommit = False,
      autoflush = False,
      bind = engine
      )
    )