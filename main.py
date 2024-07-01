from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from models import Character, ActivityEnum, HomeEnum, MoralDilemmaEnum, AdventureEnum, DemeanorEnum
from services.backstory.service import BackstoryService

app = FastAPI()


class CharacterAnswers(BaseModel):
    activity: str
    home: str
    moral_dilemma: str
    adventure: str
    demeanor: str


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    context = {
        "request": request,
        "activities": ActivityEnum,
        "homes": HomeEnum,
        "dilemmas": MoralDilemmaEnum,
        "adventures": AdventureEnum,
        "demeanors": DemeanorEnum
    }
    return templates.TemplateResponse("form.html", context=context, media_type="text/html")


app.mount("/static", StaticFiles(directory="static"), name="static")

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

