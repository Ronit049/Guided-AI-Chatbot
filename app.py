from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from chatbot import ask_llm
from memory import ConversationMemory

app = FastAPI()

memory = ConversationMemory()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )

@app.post("/chat")
async def chat(request: Request):

    data = await request.json()

    user_message = data["message"]

    memory.add("user", user_message)

    answer = ask_llm(memory.get_messages())

    memory.add("assistant", answer)

    return {
        "response": answer
    }