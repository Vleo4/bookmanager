from fastapi import FastAPI
from routes import book_routes


app = FastAPI()
app.include_router(book_routes.router)

@app.get("/")
def main_root():
    return {"Health check": "OK"}
