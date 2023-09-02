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
仮想環境としてDockerを使用する(予定)


## 起動方法
```bash
# 起動コマンド(FastAPI)
$ uvicorn app.main:app

# 起動コマンド(FastAPI x GraphQL(strawberry))
$ strawberry server app.main
```

## 参考にしたサイト類
適宜記入(備忘録)

- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/ja/)
- [DockerでFastAPIの環境を作ってGETするまで](https://zenn.dev/satonopan/articles/c4e6d55a64da0c)
- [ストロベリーを始めよう(公式Doc)](https://strawberry.rocks/docs)
- [PythonのGraphQLライブラリStrawberryを使ってみた](https://qiita.com/nttpc-aiyo/items/bb946b864e67c2da9a53)