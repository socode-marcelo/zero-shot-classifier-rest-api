import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Check if GPU is available, else use CPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

# Setting up the classifier with GPU support if available
classifier = pipeline("zero-shot-classification", model="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli", device=device)

# Pydantic model for request body validation
class ClassificationRequest(BaseModel):
    sequence_to_classify: str
    candidate_labels: list[str]

# Pydantic model for response body validation
class ClassificationResponse(BaseModel):
    labels: list[str]
    scores: list[float]

@app.get("/")
def health_check():
    return {"status": "Server is running smoothly!"}

@app.post("/classify", response_model=ClassificationResponse)
def classify_text(request: ClassificationRequest):
    try:
        output = classifier(request.sequence_to_classify, request.candidate_labels, multi_label=False)
        return {
            "labels": output["labels"],
            "scores": output["scores"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")