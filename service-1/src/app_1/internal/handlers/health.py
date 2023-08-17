from fastapi.routing import APIRouter

router: APIRouter = APIRouter()


@router.get("/health", summary="Health check.")
def find() -> str:
    """Health check."""
    return "success"
