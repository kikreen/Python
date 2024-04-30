from fastapi import FastAPI, Request, HTTPException # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.post("/analyze_sentence/")
async def analyze_sentence(request: Request):
    try:
        form_data = await request.form()
        sentence = form_data["sentence"]
        words = sentence.split()
        analysis = {
            "Количество слов": len(words),
            "Средняя длина слова": sum(len(word) for word in words) / len(words),
            "Количество уникальных слов": len(set(words)),
            "Количество символов": sum(len(word) for word in words),
            "Количество предложений": sentence.count(".")
        }
        return analysis
    except KeyError:
        raise HTTPException(status_code=400, detail="Поле 'sentence' отсутствует в запросе")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
