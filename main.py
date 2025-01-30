from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/", status_code=200)
def get_info():
    """Returns the registered email, current datetime, and GitHub URL."""
    return {
        "email": "goodnewsagijesuefe@gmail.com",
        "timestamp": datetime.utcnow().isoformat() + "Z",  # Ensuring UTC format
        "github_url": "https://github.com/goodnews22r/Public-API.git",
    }
