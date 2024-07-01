import openai


class BaseClient:
    def generate_text(self, prompt):
        raise NotImplementedError("generate_text method is not implemented")


class OpenAIClient(BaseClient):
    prompt: str

    def __init__(self, api_key):
        openai.api_key = api_key
        with open("services/backstory/prompt.txt", "r") as file:
            self.prompt = file.read()

    def generate_text(self, prompt):
        return openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": "What is your name?"},
            ]
        )


class DummyClient(BaseClient):
    def generate_text(self, prompt):
        return "This is a dummy response for the prompt: " + prompt
