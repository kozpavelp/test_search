import uvicorn
from fastapi import FastAPI, APIRouter

from handlers.search_handlers import search_router

app = FastAPI()
main_router = APIRouter()

main_router.include_router(search_router, prefix='/search', tags=['search'])
app.include_router(main_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)