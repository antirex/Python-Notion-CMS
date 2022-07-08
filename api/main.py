import uvicorn
from fastapi import FastAPI
from config import settings

from endpoints.routers import router as thought_experiments_router


app = FastAPI()


@app.get("/", tags=["Endpoint test"])
def read_root():
    return {"message": "welcome to notion CMS backend"}


app.include_router(thought_experiments_router, tags=["notion"], prefix="/api")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
