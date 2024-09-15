from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: str

    @property
    def get_bot_token(self) -> str:
        return self.BOT_TOKEN

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
