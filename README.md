# graphql-python-practice
python(FW:FastAPI), graphqlの練習リポジトリ

## 使用言語/フレームワーク/バージョンなど
| -              | -          | バージョン | 備考                          | 
| -------------- | ---------- | ---------- | ----------------------------- | 
| 言語            | python     | 3.11.4     |                               | 
| フレームワーク    | FastAPI    | 0.103.0    | https://fastapi.tiangolo.com/ | 
| API            | GraphQL    | -          |                               | 
| フレームワーク    | Strawberry |            | https://strawberry.rocks/     | 
| ORM            | sqlalchemy |            | https://www.sqlalchemy.org/   | 


## その他
### Docker
- mysqlをdockerに作成


## 起動方法
```bash
# 起動コマンド(FastAPI)
$ uvicorn app.main:app

# 起動コマンド(FastAPI x GraphQL(strawberry))
$ strawberry server app.main
```

## 起動方法(Docker)
```bash
# docker起動
$ docker-compose up -d

# docker削除(volumes削除, 削除しない場合は-v無しで実行)
$ docker-compose down -v

# DB 初期化
$ zsh ./docker/mysql/init_mysql_db.sh

# コンテナにログイン
$ docker exec -it mysql-container bash

# MySQLにログイン
$ mysql -u root -p

```

## 参考にしたサイト類
適宜記入(備忘録)

- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/ja/)
- [DockerでFastAPIの環境を作ってGETするまで](https://zenn.dev/satonopan/articles/c4e6d55a64da0c)
- [ストロベリーを始めよう(公式Doc)](https://strawberry.rocks/docs)
- [PythonのGraphQLライブラリStrawberryを使ってみた](https://qiita.com/nttpc-aiyo/items/bb946b864e67c2da9a53)
- [Python+SQLAlchemy+MySQLでDB接続](https://financial-it-engineer.hatenablog.com/entry/20170112/1484220341)
- [【SQLAlchemy】Generic Typesと各種DBの型 対応表
](https://zenn.dev/re24_1986/articles/8520ac3f9a0187)
- [【Python 】pymysqlで「RuntimeError: cryptography is required for sha256_password...」の解消方法！](https://akizora.tech/pymysql-cryptography-required-4236)