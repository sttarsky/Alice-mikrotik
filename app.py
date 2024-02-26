from models import Post, Response
from fastapi import FastAPI
from parser import parser

app = FastAPI(title="Alice", docs_url=None, redoc_url=None)


@app.post("/")
async def ask(request: Post) -> Response:
    result = await parser(request)
    return result



