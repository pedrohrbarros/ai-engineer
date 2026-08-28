from fastapi import FastAPI, Request

app = FastAPI()

@app.post(
    "/query",
    status_code=200
)
async def query(
    request: Request
):
    return {
        "message": "AI Engineer interview"
    }