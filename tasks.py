from models import TranslationModel
from transformers import T5Tokenizer, T5ForConditionalGeneration


## Tasks that w will be  running on the Backed

## Store translation Task => Take translation request and seve it to the DB
def store_translation(t):
    model = TranslationModel(text=t.text, base_lang=t.base_lang, final_lang=t.final_lang)
    model.save()
    return model.id

## Run Translation Task => run a deep learning Model

# Find translation Task => Retrieve the translation from the DB