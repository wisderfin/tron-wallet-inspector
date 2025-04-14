from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # database
    DATABASE_DRIVER: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_HOST: str

    API_PORT: int
    API_HOST: str

    TRONGRID_API_KEY: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
