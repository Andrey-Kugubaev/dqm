from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'APP_TITLE'
    description: str = 'DESCRIPTION'
    database_url: str
    model_config = ConfigDict(env_file='.env')


settings = Settings()
