from fastapi.routing import APIRouter

router: APIRouter = APIRouter()


@router.get("/health", summary="")
def find() -> str:
    return "success"
