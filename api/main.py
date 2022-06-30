import uvicorn
from fastapi import FastAPI
from .config import settings 

app = FastAPI()

@app.get("/", tags=["Health test"])
def read_root():
    return {"message": "Healthy"}

app.include_router(notion_fetch_router, tags=["notion"], prefix="/api")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
