import os

from services.backstory.clients import DummyClient, OpenAIClient, BaseClient


def get_client() -> BaseClient:
    if os.getenv("ENVIRONMENT") == "test":
        return DummyClient()
    else:
        return OpenAIClient(os.getenv("OPENAI_API_KEY"))


client = get_client()
