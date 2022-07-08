from fastapi import APIRouter
from app.ThoughtExperiments.thought_experiments_handler import ThoughtExperimentsHandler


# router object for handling api routes
router = APIRouter()


@router.get("/thought-experiments", response_description="List all posts")
async def list_posts():
    thought_experiments = await ThoughtExperimentsHandler().get_articles()
    return thought_experiments


@router.get(
    "/thought-experiments/{name}",
    response_description="List thought experiment based on name",
)
async def show_named_post():
    pass


@router.get("/{id}", response_description="Get a single post")
async def show_post(id: str):
    pass
