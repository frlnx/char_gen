from openai import AsyncOpenAI


class BaseClient:
    async def generate_text(self, answers):
        raise NotImplementedError("generate_text method is not implemented")


class OpenAIClient(BaseClient):
    prompt: str
    client: AsyncOpenAI

    def __init__(self, api_key):
        self.client = AsyncOpenAI(
            # This is the default and can be omitted
            api_key=api_key,
        )
        with open("services/backstory/prompt.txt", "r") as file:
            self.prompt = file.read()

    async def generate_text(self, answers):
        response = await self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": answers},
            ]
        )
        return response.choices[0].message.text


class DummyClient(BaseClient):
    async def generate_text(self, answers):
        return "You are King Arthur, a knight of the Round Table. You are on a quest to find the Holy Grail."
