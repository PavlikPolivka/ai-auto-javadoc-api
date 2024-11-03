from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

app = FastAPI()

model_path = "/app/model" 
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

class CodeInput(BaseModel):
    code: str

@app.get("/")
async def health_check():
    return {"status": "running"}

@app.post("/generate_javadoc")
async def generate_javadoc(code_input: CodeInput):
    try:
        inputs = tokenizer(code_input.code, return_tensors="pt")
        outputs = model.generate(**inputs)
        javadoc = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"javadoc": javadoc}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))