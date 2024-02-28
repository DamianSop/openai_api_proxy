from fastapi import APIRouter, Depends, HTTPException
from starlette import status

import schemas
from utils import openai_api
from utils.config import settings
from utils.loggers import get_module_logger
from utils.auth import authorize

logger = get_module_logger(__name__)

query_router = APIRouter(prefix="/query", tags=['query'])


@query_router.post('/chat_completions')
async def chat_completions(data: schemas.ChatCompletions, api_keys: list[str] = Depends(authorize)):

    api_keys = openai_api.get_api_keys(api_keys)
    if data.tools is None:
        data.tool_choice = None
    return await openai_api.chat_completions(data, api_keys)


@query_router.post('/image_generation')
async def image_generation(data: schemas.ImageGeneration, api_keys: list[str] = Depends(authorize)):
    api_keys = openai_api.get_api_keys(api_keys)
    return await openai_api.image_generation(data, api_keys)


