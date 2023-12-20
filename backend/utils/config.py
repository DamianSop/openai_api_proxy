import os

from dotenv import load_dotenv
from pathlib import Path

from pydantic.v1 import BaseSettings

load_dotenv(dotenv_path=Path('../../.env'))


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    use_env_openai_keys: bool = os.getenv("USE_KEYS") if os.getenv("USE_KEYS") else False
    use_auth_token: bool | None = os.getenv("USE_AUTH_TOKEN") if os.getenv("USE_AUTH_TOKEN") else None
    auth_token: str | None = None
    model_text: str = os.getenv("MODEL_TEXT") if os.getenv("MODEL_TEXT") else "gpt-3.5-turbo-1106"
    model_image: str = os.getenv("MODEL_IMAGE") if os.getenv("MODEL_IMAGE") else "dall-e-2"
    open_ai_keys: list[str] | None = os.getenv("OPENAI_KEYS").split(' ') if os.getenv("OPENAI_KEYS") else None


settings = Settings()
