import sqlalchemy

from app.data import base;

class Users(base.Base): 
    __tablename__ = 'users_table'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(50))
    last_name = sqlalchemy.Column(sqlalchemy.String(50))
    first_name_kana = sqlalchemy.Column(sqlalchemy.String(50))
    last_name_kana = sqlalchemy.Column(sqlalchemy.String(50))
    age = sqlalchemy.Column(sqlalchemy.Integer)
    gender = sqlalchemy.Column(sqlalchemy.Integer)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime)