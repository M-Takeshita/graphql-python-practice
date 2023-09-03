import sqlalchemy

#engine = sqlalchemy.create_engine("{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?{queryparam}")
# TODO: envファイル管轄にする
engine = sqlalchemy.create_engine("mysql+pymysql://user:userpassword@localhost:3306/python_practice_database")