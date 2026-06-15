# RegRadar

A starter project for the RegRadar hackathon build. This repository includes a backend and frontend scaffold for RBI circular ingestion and impact reporting.

## Structure

- `backend/`: FastAPI backend scaffold
- `frontend/`: React frontend scaffold

## Get started

1. Open this repository in VS Code.
2. Start the backend:
   - `cd backend`
   - `python -m venv .venv`
   - `source .venv/Scripts/activate` (Windows PowerShell: `.\.venv\Scripts\Activate.ps1`)
   - `pip install -r requirements.txt`
   - `uvicorn main:app --reload --host 0.0.0.0 --port 8000`
3. Start the frontend:
   - `cd frontend`
   - `npm install`
   - `npm start`

## Notes

This scaffold includes basic startup endpoints and a simple React dashboard for future RBI circular ingestion, agent orchestration, and report display.
