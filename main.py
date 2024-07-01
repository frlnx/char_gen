from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.responses import HTMLResponse

from models import Character, ActivityEnum, HomeEnum, MoralDilemmaEnum, AdventureEnum, DemeanorEnum
from services.backstory.service import BackstoryService

app = FastAPI()


class CharacterAnswers(BaseModel):
    activity: int
    home: int
    moral_dilemma: int
    adventure: int
    demeanor: int


@app.get("/", response_class=HTMLResponse)
async def get_form():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Create a DnD Character</title>
    </head>
    <body>
        <h1>Create Your DnD Character</h1>
        <form action="/create-character/" method="post">
            <label for="activity">Which of these activities would your character excel at during their free time?</label><br>
            <select id="activity" name="activity">
                <option value="1">Practicing weapon techniques</option>
                <option value="2">Sneaking and gathering information</option>
                <option value="3">Studying ancient tomes and practicing spells</option>
                <option value="4">Performing rituals and healing others</option>
                <option value="5">Exploring the wilderness and tracking creatures</option>
            </select><br><br>
            <label for="home">Where did your character grow up?</label><br>
            <select id="home" name="home">
                <option value="1">A bustling human city</option>
                <option value="2">An enchanting forest village</option>
                <option value="3">A stronghold carved into the mountains</option>
                <option value="4">A cozy underground burrow</option>
                <option value="5">A mystical, floating island or temple</option>
                <option value="6">A remote desert oasis</option>
            </select><br><br>
            <label for="moral_dilemma">How does your character approach a moral dilemma?</label><br>
            <select id="moral_dilemma" name="moral_dilemma">
                <option value="1">Follow the rules and do what's right</option>
                <option value="2">Do what feels right in the moment, regardless of rules</option>
                <option value="3">Weigh the situation carefully and act for the greater good</option>
                <option value="4">Use whatever means necessary to achieve their goal</option>
                <option value="5">Avoid taking sides and stay neutral</option>
            </select><br><br>
            <label for="adventure">What motivates your character to embark on an adventure?</label><br>
            <select id="adventure" name="adventure">
                <option value="1">A mission to avenge the fallen</option>
                <option value="2">A journey to protect loved ones from harm</option>
                <option value="3">An expedition to uncover forgotten knowledge and secrets</option>
                <option value="4">A venture in search of legendary treasures</option>
                <option value="5">A campaign to overthrow a powerful tyrant</option>
                <option value="6">A pilgrimage to fulfill a sacred duty or prophecy</option>
            </select><br><br>
            <label for="demeanor">Which of these traits best describes your character's demeanor?</label><br>
            <select id="demeanor" name="demeanor">
                <option value="1">A brave leader who inspires others</option>
                <option value="2">A charming individual who can talk their way out of anything</option>
                <option value="3">A perceptive and intelligent individual always seeking answers</option>
                <option value="4">A compassionate healer with a heart of gold</option>
                <option value="5">A rugged and self-sufficient outdoorsman</option>
                <option value="6">A fierce warrior with a short temper</option>
                <option value="7">A creative artist with a knack for performance</option>
                <option value="8">A mystical and insightful person deeply connected to nature</option>
                <option value="9">A disciplined and honorable warrior following a strict code</option>
                <option value="10">A mysterious and enigmatic figure with a sinister edge</option>
            </select><br><br>
            <input type="submit" value="Create Character">
        </form>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/create-character/")
async def create_character(answers: CharacterAnswers):
    return "Not implemented"
