from fastapi import FastAPI # type: ignore (venv)
from app.routes import routes
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(routes.router)

origins = [
    "http://localhost:5173",  # Vite dev server
    "http://localhost:5174",  # Vite dev server (alternative port)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # You can also use ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods: POST, GET, OPTIONS, etc.
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message" : "App running"}