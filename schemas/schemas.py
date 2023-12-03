from pydantic import BaseModel
from typing import List


class SearchQuery(BaseModel):
    query: str


class SearchResponse(BaseModel):
    themes: List[str]
