from typing import Annotated

from fastapi import Header, HTTPException
from starlette import status

from .config import settings


def authorize(
        token: Annotated[str | None, Header(alias="x-auth-token")] = None,
        openai_api_keys: Annotated[str | None, Header(alias="open-ai-keys")] = None
):
    if settings.use_auth_token and token == settings.auth_token or not settings.use_auth_token:
        return openai_api_keys.split(' ') if openai_api_keys else None
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalid"
        )
