from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/", status_code=200)
def get_info():
    """
    Returns the registered email, dynamically generated datetime (ISO 8601 UTC), and GitHub URL.
    """
    return {
        "email": "goodnewsagijesuefe@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",  # ISO 8601 format
        "github_url": "https://github.com/goodnews22r/Public-API",
    }

