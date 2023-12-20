from contextlib import asynccontextmanager
import secrets
from fastapi import FastAPI
from routers.query import query_router
import uvicorn
from utils.loggers import get_module_logger
from utils.config import settings

logger = get_module_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.use_auth_token:
        token = secrets.token_hex(32)
        settings.auth_token = token
        with open('generations/token.txt', 'w') as f:
            f.write(token)
    yield


app = FastAPI(version='1', lifespan=lifespan)
app.include_router(query_router, prefix=settings.api_v1_prefix)

if __name__ == '__main__':
    uvicorn.run(
        '__main__:app',
        host="0.0.0.0",
        port=3501
    )
