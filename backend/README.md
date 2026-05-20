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

## Example Advisory Request

```json
{
  "crop": "Tomato",
  "district": "Nashik",
  "language": "English",
  "question": "My tomato leaves have yellow spots. What should I do?"
}
```

