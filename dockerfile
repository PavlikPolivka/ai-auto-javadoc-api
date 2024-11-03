FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install huggingface-hub transformers

RUN python -c "from transformers import AutoModelForSeq2SeqLM, AutoTokenizer; \
    model = AutoModelForSeq2SeqLM.from_pretrained('PavelPolivka/javadocer-small'); \
    tokenizer = AutoTokenizer.from_pretrained('PavelPolivka/javadocer-small'); \
    model.save_pretrained('/app/model'); \
    tokenizer.save_pretrained('/app/model')"

# Copy the rest of the application code into the container
COPY . .

# Expose the FastAPI app's port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]