from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json

# Initialize FastAPI app
app = FastAPI()

# Load model and tokenizer
model = load_model('model.h5')

# Load the JSON from the file
with open('tokenizer.json', 'r') as f:
    tokenizer_json = f.read()

# Convert JSON back to a Tokenizer object
tokenizer = tokenizer_from_json(tokenizer_json)

# Sequence length for padding
sequence_length = 5

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

def generate_quote(seed_text, next_words, model, max_sequence_len):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = model.predict(token_list, verbose=0)
        predicted_word_index = np.argmax(predicted, axis=1)[0]
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted_word_index:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, seed_text: str = Form(...), num_words: int = Form(...)):
    quote = generate_quote(seed_text, num_words, model, sequence_length)
    print(quote)
    return templates.TemplateResponse("index.html", {"request": request, "quote": quote, "seed_text": seed_text, "num_words": num_words,"seed_text":seed_text})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
