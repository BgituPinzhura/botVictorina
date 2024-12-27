from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


# Создание класса для токена бота для безопасности
class Settings(BaseSettings):
    bot_token: SecretStr
    
    model_config = SettingsConfigDict(env_file="config/.env", env_file_encoding="utf-8", validate_default=False)
