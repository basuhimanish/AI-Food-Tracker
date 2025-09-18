# AI Food Tracker

Backend: FastAPI + SQLAlchemy + Alembic (PostgreSQL). Frontend: Vite + React (JS in `frontend`, TS+Tailwind in `frontend2`).

## Prerequisites
- Python 3.10+
- Node.js 18+ and npm
- PostgreSQL instance
- Git

## 1) Clone
```bash
git clone https://github.com/basuhimanish/AI-Food-Tracker.git
cd AI-Food-Tracker
```

## 2) Backend setup (FastAPI)
```bash
# Windows PowerShell
python -m venv venv
venv\Scripts\activate

# Install deps
pip install -r requirements.txt
```

Create a `.env` file in the project root:
```env
# Example — change values to your DB
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@HOST:5432/DB_NAME
```

Run DB migrations:
```bash
alembic upgrade head
```

Start API server:
```bash
uvicorn app.main:app --reload
# or: .\start_server.bat (Windows)
```
API default: http://127.0.0.1:8000

## 3) Frontend setup (Vite + React)
Expect the API at http://localhost:8000 and FastAPI CORS is preconfigured for Vite ports 5173/5174.

`frontend2` (TypeScript + Tailwind):
```bash
cd frontend2
npm install
npm run dev
```

Vite shows a local URL like http://localhost:5173.

## Project Structure (high-level)
- `app/main.py` — FastAPI app + CORS
- `app/database.py` — SQLAlchemy engine/session, reads `DATABASE_URL` from `.env`
- `alembic/` — migrations
- `frontend/` — React (JS)
- `frontend2/` — React (TS)

## Common Commands
- New migration: `alembic revision -m "message" --autogenerate`
- Apply migrations: `alembic upgrade head`

## Troubleshooting
- Connection errors: verify `DATABASE_URL` and DB reachability
- CORS: ensure frontend runs on 5173/5174 or update `allow_origins` in `app/main.py`
- If `psycopg2` compile fails, `psycopg2-binary` is included in requirements
