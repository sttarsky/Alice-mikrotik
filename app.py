from fastapi import FastAPI, HTTPException
from parser import parser
app = FastAPI(title="Alice")


@app.post("/")
async def ask(request):
    result = await parser(request)
    return result[1]


@app.get("/")
async def default():
    raise HTTPException(status_code=404, detail="Item not found")




