import asyncio

import openai
from fastapi import HTTPException
from openai import OpenAI
from starlette import status

import schemas
from .config import settings
from .loggers import get_module_logger

logger = get_module_logger(__name__)


def get_api_keys(api_keys: list[str] | None) -> list[str]:
    if api_keys is None and settings.open_ai_keys is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OpenAI API Key not found.")
    elif api_keys is None:
        api_keys = settings.open_ai_keys
    return api_keys


def next_api_key(api_keys: list[str], key_index: int):
    if key_index == len(api_keys) - 1:
        key_index = 0
    else:
        key_index += 1
    return key_index


def openai_request(func):
    async def wrapper(data, api_keys):
        client = OpenAI(api_key=api_keys[0])
        key_index = 0

        while True:
            try:
                return func(data, api_keys, client)
            except (
                    openai.AuthenticationError,
                    openai.NotFoundError,
                    openai.APIError
            ) as e:

                logger.error(e)
                raise HTTPException(status_code=e.status_code, detail=e.message)

            except openai.RateLimitError as e:
                logger.error(e)

                await asyncio.sleep(30)
                key_index = next_api_key(api_keys, key_index)
                client.api_key = api_keys[key_index]
    return wrapper


@openai_request
def chat_completions(data: schemas.ChatCompletions, api_keys: list[str], client: OpenAI = None):
    return client.chat.completions.create(**data.model_dump())


@openai_request
def image_generation(data: schemas.ImageGeneration, api_keys: list[str], client: OpenAI = None):
    return client.images.generate(**data.model_dump())


