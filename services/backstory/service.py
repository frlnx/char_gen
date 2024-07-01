from models import Character


class BackstoryService:
    def __init__(self):
        from services.backstory.provider import client
        self.client = client

    async def get_backstory(self, answers: Character):
        prompt = (f"My character is a {answers.activity} "
                  f"who grew up in {answers.home}. "
                  f"They approach moral dilemmas by {answers.moral_dilemma} "
                  f"and are motivated to embark on an adventure by {answers.adventure}. "
                  f"Their demeanor is {answers.demeanor}.")
        backstory = self.client.get_backstory(prompt)
        return backstory
