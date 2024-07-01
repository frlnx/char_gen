from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.responses import HTMLResponse, FileResponse

from models import Character, ActivityEnum, HomeEnum, MoralDilemmaEnum, AdventureEnum, DemeanorEnum
from services.backstory.service import BackstoryService

app = FastAPI()


class CharacterAnswers(BaseModel):
    activity: str
    home: str
    moral_dilemma: str
    adventure: str
    demeanor: str


@app.get("/", response_class=HTMLResponse)
async def get_form():
    activity_options = "</option><option value=\"".join([f"{activity.name}\">{activity.value}" for activity in ActivityEnum])
    home_options = "</option><option value=\"".join([f"{home.name}\">{home.value}" for home in HomeEnum])
    moral_dilemma_options = "</option><option value=\"".join([f"{moral_dilemma.name}\">{moral_dilemma.value}" for moral_dilemma in MoralDilemmaEnum])
    adventure_options = "</option><option value=\"".join([f"{adventure.name}\">{adventure.value}" for adventure in AdventureEnum])
    demeanor_options = "</option><option value=\"".join([f"{demeanor.name}\">{demeanor.value}" for demeanor in DemeanorEnum])

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Create a DnD Character</title>
        <script src="static/formHandler.js"></script>
    </head>
    <body>
        <h1>Create Your DnD Character</h1>
        <form action="/create-character/" method="post" id="characterForm">
            <label for="activity">Which of these activities would your character excel at during their free time?</label><br>
            <select id="activity" name="activity">
                {activity_options}

            </select><br><br>
            <label for="home">Where did your character grow up?</label><br>
            <select id="home" name="home">
                {home_options}
            </select><br><br>
            <label for="moral_dilemma">How does your character approach a moral dilemma?</label><br>
            <select id="moral_dilemma" name="moral_dilemma">
                {moral_dilemma_options}
            </select><br><br>
            <label for="adventure">What motivates your character to embark on an adventure?</label><br>
            <select id="adventure" name="adventure">
                {adventure_options}
            </select><br><br>
            <label for="demeanor">Which of these traits best describes your character's demeanor?</label><br>
            <select id="demeanor" name="demeanor">
                {demeanor_options}
            </select><br><br>
            <input type="submit" value="Create Character">
        </form>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/static/formHandler.js")
async def serve_static_files():
    return FileResponse("static/formHandler.js")

@app.post("/create-character/")
async def create_character(answers: CharacterAnswers):
    character = Character(
        activity=ActivityEnum[answers.activity],
        home=HomeEnum[answers.home],
        moral_dilemma=MoralDilemmaEnum[answers.moral_dilemma],
        adventure=AdventureEnum[answers.adventure],
        demeanor=DemeanorEnum[answers.demeanor]
    )
    backstory_service = BackstoryService()
    return await backstory_service.get_backstory(character)

