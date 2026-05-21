# Agri-AI Backend

FastAPI backend for the Agri-AI demo dashboard.

## Run Locally

```powershell
cd "D:\agentic project\farmer\backend"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## API Routes

- `GET /` basic backend info
- `GET /health` health check
- `GET /agents` available agent modules
- `POST /advisory` mock orchestrator advisory response
- `POST /disease/analyze` image upload disease analysis response
- `POST /weather/risk` district weather risk response

## Backend Structure

```text
backend/
├── main.py                  FastAPI routes and CORS setup
├── schemas.py               Pydantic request/response models
├── orchestrator.py          Combines specialist agent outputs
└── services/
    ├── disease_agent.py     Crop symptom and disease-risk logic
    ├── weather_agent.py     Weather-risk advisory logic
    └── market_agent.py      Mandi price signal logic
```

The frontend calls `/advisory`. FastAPI sends the request to the orchestrator. The orchestrator runs the disease, weather, and market agents, then merges their outputs into one farmer advisory.

## Example Advisory Request

```json
{
  "crop": "Tomato",
  "district": "Nashik",
  "language": "English",
  "question": "My tomato leaves have yellow spots. What should I do?"
}
```
