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



## Index Route => Test if this route is working
@app.get("/")
def get_root():
    return {"message: Hello World"}

## Translate Route => Take in a translate request, return a translation, and store it on the DB


## Results route => Take in a translation ID, and return the translated text