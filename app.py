from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(title="Digit Wordifier", version="v1")

class Health(BaseModel):
    ok: bool

class DigitWordifyResponse(BaseModel):
    input: str
    wordified: str

digit_names = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/digit-wordify", response_model=DigitWordifyResponse)
def digit_wordify(text: str = Query(..., description="Text including digits to wordify")):
    wordified = " ".join(digit_names[ch] for ch in text if ch in digit_names)
    return {"input": text, "wordified": wordified}
