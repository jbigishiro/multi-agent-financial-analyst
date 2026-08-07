from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    openai_api_key: str
    tavily_api_key: str
    langsmith_api_key : str

    model_name: str = "gpt-5-mini"
    temperature: float = 0.2
    max_tokens: int = 2000

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()