from models import TranslationModel
from transformers import T5Tokenizer, T5ForConditionalGeneration


tokenizer = T5Tokenizer.from_pretrained("t5-small", model_max_length=512)
translator = T5ForConditionalGeneration.from_pretrained("t5-small")


# Tasks that w will be  running on the Backed

# Store translation Task => Take translation request and seve it to the DB
def store_translation(t):
    model = TranslationModel(
        text=t.text, base_lang=t.base_lang, final_lang=t.final_lang)
    model.save()
    return model.id

# Run Translation Task => run a deep learning Model


def run_translation(t_id: int):
    model = TranslationModel.get_by_id(t_id)

    prefix = f"translate {model.base_lang} to {model.final_lang}: {model.text}"
    input_ids = tokenizer(prefix, return_tensors="pt").input_ids
    outputs = translator.generate(input_ids, max_new_tokens=512)
    translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    model.translation = translation
    model.save()

# Find translation Task => Retrieve the translation from the DB


def find_translation(t_id: int):
    model = TranslationModel.get_by_id(t_id)
    translation = model.translation
    if translation is None:
        translation = "Processing, check back later."
    return translation
