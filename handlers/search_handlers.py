from fastapi import APIRouter
from schemas.schemas import SearchQuery, SearchResponse
from actions.actions import define_themes

search_router = APIRouter()


@search_router.post('/', response_model=SearchResponse)
async def search_themes(query: SearchQuery):
    result = define_themes(query.query)
    return {'themes': result}
