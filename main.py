from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, validator
import tasks

app = FastAPI()

languages = ["English", "German", "French", "Russian"]


class Translation(BaseModel):
    text: str
    base_lang: str
    final_lang: str

    @validator('base_lang', 'final_lang')
    def valid_lang(cls, lang):
        if lang not in languages:
            raise ValueError("Invalid Language")
        return lang


# Index Route => Test if this route is working
@app.get("/")
def get_root():
    return {"message: Hello World"}

# Translate Route => Take in a translate request, return a translation, and store it on the DB
@app.post("/translate")
def post_translation(t: Translation, background_tasks: BackgroundTasks):
    t_id = tasks.store_translation(t)
    background_tasks.add_task(tasks.run_translation, t_id)
    return {"task_id": t_id}



# Results route => Take in a translation ID, and return the translated text
@app.get("/results")
def get_translation(t_id: int):
    return {"translation": tasks.find_translation(t_id)}