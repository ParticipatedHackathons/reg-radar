from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, Response
from pydantic import BaseModel


app = FastAPI(title="RegRadar Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class StatusResponse(BaseModel):
    status: str
    message: str

@app.get("/api/status", response_model=StatusResponse)
def status():
    return {"status": "ok", "message": "RegRadar backend is running."}

class DirectiveRequest(BaseModel):
    text: str

class DirectiveResponse(BaseModel):
    directives: list[str]

@app.post("/api/extract-directions", response_model=DirectiveResponse)
def extract_directions(request: DirectiveRequest):
    # Placeholder for RBI circular parsing / directive extraction logic
    if not request.text.strip():
        return {"directives": []}
    return {"directives": ["Placeholder directive 1", "Placeholder directive 2"]}


@app.get("/")
def root():
    # Redirect root to the status endpoint for a friendly default
    return RedirectResponse(url="/api/status")


@app.get("/favicon.ico")
def favicon():
    # Return no content for favicon requests to avoid 404 noise
    return Response(status_code=204)
