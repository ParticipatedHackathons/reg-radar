# implement routes
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class StatusResponse(BaseModel):
    status: str
    message: str

@router.get("/status", response_model=StatusResponse)
def status():
    return {"status": "ok", "message": "RegRadar backend is running."}

class DirectiveRequest(BaseModel):
    text: str

class DirectiveResponse(BaseModel):
    directives: list[str]

@router.post("/extract-directions", response_model=DirectiveResponse)
def extract_directions(request: DirectiveRequest):
    # Placeholder for RBI circular parsing / directive extraction logic
    if not request.text.strip():
        return {"directives": []}
    return {"directives": ["Placeholder directive 1", "Placeholder directive 2"]}
