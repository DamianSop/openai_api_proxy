from typing import Optional, Annotated

from fastapi import UploadFile, File
from pydantic import BaseModel, RootModel, field_validator, Field
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


class Properties(RootModel):
    root: dict[str, dict]


class Parameters(BaseModel):
    type: str
    properties: Properties
    required: list[str] | None = None


class Function(BaseModel):
    name: str


class FunctionFull(Function):
    description: str | None = None
    parameters: Parameters | None = None


class Tool(BaseModel):
    type: str = 'function'
    function: Function


class ToolFull(BaseModel):
    type: str = 'function'
    function: FunctionFull


class ChatCompletions(BaseModel):
    model: str = settings.model_text
    max_tokens: int | None = None
    messages: list[Message]
    tools: list[ToolFull] | None = None
    tool_choice: str | None | Tool = 'auto'


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
