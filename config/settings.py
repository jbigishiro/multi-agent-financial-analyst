from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_api_key: str
    tavily_api_key: str
    model_name: str = "gpt-4.O-mini"
    temperature: float = 0.2
    api_title: str = "Multi-Agent Financial Analyst"
    api_version: str = "1.0.0"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()