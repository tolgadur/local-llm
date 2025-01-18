from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import LOCAL_MODEL_CPU
import uvicorn

app = FastAPI(title="Local LLM API")


class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = 50


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/generate")
def generate_text(request: GenerateRequest):
    try:
        response = LOCAL_MODEL_CPU(request.prompt, max_new_tokens=request.max_tokens)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
