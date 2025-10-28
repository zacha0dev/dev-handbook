# app/core/settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # Accept both lower/upper keys, read .env, and ignore unrelated keys
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    # Prefer pythonic snake_case field names; map to UPPER env names via alias
    app_name: str = Field(default="My Azure API", alias="APP_NAME")
    app_version: str = Field(default="0.1.0", alias="APP_VERSION")
    environment: str = Field(default="development", alias="ENVIRONMENT")
    pepper: str = Field(default="pepper", alias="PEPPER")
    bcrypt_rounds: int = Field(default=12, alias="BCRYPT_ROUNDS")
    log_level: str = Field(default="debug", alias="LOG_LEVEL")

settings = Settings()