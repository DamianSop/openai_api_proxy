from fastapi import UploadFile, File
from pydantic import BaseModel
from utils.config import settings


class ImageUrl(BaseModel):
    url: str
    detail: str


class Content(BaseModel):
    type: str
    text: str | None
    image_url: ImageUrl | None


class Message(BaseModel):
    role: str
    content: str | Content


class ChatCompletions(BaseModel):
    model: str = settings.model_text
    max_tokens: int = 1024
    messages: list[Message]


class ImageGeneration(BaseModel):
    model: str = settings.model_image
    prompt: str
    size: str = "1024x1024"
    quality: str = "standard"
    n: int = 1
    response_format: str | None = "url"
    '''
     The style of the generated images. Must be one of vivid or natural. 
     Vivid causes the model to lean towards generating hyper-real and dramatic images. 
     Natural causes the model to produce more natural, less hyper-real looking images. 
     This param is only supported for dall-e-3.
    '''
    style: str | None = None
