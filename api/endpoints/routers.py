from fastapi import APIRouter, HTTPException, Request

#router object for handling api routes
router = APIRouter()

@router.get("/", response_description="List all posts")
async def list_posts(request: Request):
    pass


@router.get("/{name}", response_description="List post based on name")
async def show_named_post():
    pass


@router.get("/{id}", response_description="Get a single post")
async def show_post(id: str):
    pass


