import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

msg = {
    'msg': 'Welcome to FastAPI + Graph QL Template',
    'info':'visit http://localhost:<port>/graphql for GraphiQL UI.',
    'link':'https://et-dev.firstam.com'
    }

app = FastAPI()
@strawberry.type
class User:
    name: str
    age: int
    title: str

@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Tony Stark", age=48, title='Iron Man')


schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

@app.get("/")
async def root():
    return msg

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
