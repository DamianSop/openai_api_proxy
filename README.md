# OpenAI API Proxy

## Introduction
OpenAI API Proxy is a project designed to provide access to the OpenAI API from countries where official support is not available. To use this proxy application, it needs to be deployed on a server in a country where OpenAI is supported.

## Technologies Used
This project uses the following technologies:
- Python
- FastAPI
- Docker

## Installation and Usage
To install and use this project, follow these steps:
1. Clone the repository to your local computer.
2. Add the necessary data to the `.env` file. If you don't have specific data, you can leave it empty.
3. Start the server using `docker-compose`.

### Available Parameters
- `USE_KEYS=True`: Use keys from .env for requests without keys.
- `OPENAI_KEYS='API_Key_1 API_Key_2 API_Key_3'`: OpenAI keys can be added multiple through space. If you are using the trial version, then at RateLimitError, the next keys in the list will be used.
- `USE_AUTH_TOKEN=True`: If True, then when making requests to the application, you need to pass the x-auth-token header parameter with the token, which will be generated in the generations/token.txt file during initialization.
- `MODEL_TEXT='gpt-3.5-turbo-1106'`: The default gpt model that will be used if you do not pass the model in the requests.
- `MODEL_IMAGE='dall-e-2'`: The default model for generating images that will be used if you do not pass the model in the requests.

You can also pass OpenAI keys through the `open-ai-keys` header parameter in your requests. The keys should be separated by spaces. However, please note that passing keys over HTTP is not secure, so it is recommended to do this over HTTPS.

You can leave the file empty to use the default parameters:
- `USE_KEYS=False`
- `USE_AUTH_TOKEN=False`
- `OPENAI_KEYS=None`
- `MODEL_TEXT='gpt-3.5-turbo-1106'`
- `MODEL_IMAGE='dall-e-2'`

## Help and Support
If you encounter any problems or have questions about using this project, please create a new issue in the "Issues" section of this repository.
