from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, Response
from api import routes


app = FastAPI(title="RegRadar Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(routes.router, tags=["Agents"], prefix="/api")

@app.get("/")
def root():
    # Redirect root to the status endpoint for a friendly default
    return {"Welcome to RegRadar APIs"}


@app.get("/favicon.ico")
def favicon():
    # Return no content for favicon requests to avoid 404 noise
    return Response(status_code=204)
