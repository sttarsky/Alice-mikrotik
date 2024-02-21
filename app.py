from models import Post
from fastapi import FastAPI, HTTPException
from parser import parser
app = FastAPI(title="Alice")


@app.post("/")
async def ask(request: Post):
    result = await parser(request)
    response = {
        'response': {
            'text': result[1],
            'end_session': True
        },
        'version': request.version
    }
    return response




@app.get("/")
async def default():
    raise HTTPException(status_code=404, detail="Item not found")




