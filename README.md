# Public-API
This is a simple API that returns the registered email, the current UTC datetime in ISO 8601 format, and a link to the GitHub repository for the project. The API is built using FastAPI.

# Features
Email: Returns the registered email address.
Timestamp: Returns the current UTC timestamp in ISO 8601 format.
GitHub URL: Provides a link to the project’s GitHub repository.
# Setup Instructions
To run the project locally, follow these steps BELOW:

# Prerequisites
Make sure you have the following installed:
Python 3.7 or higher
pip (Python package installer)

# Install Dependencies
Clone this repository or download the project files.
Navigate to the project directory and install the required Python dependencies:
pip install fastapi uvicorn

# Run the Application Locally
To run the FastAPI application, use Uvicorn as the ASGI server:
uvicorn main:app --reload
This will start the server locally on http://127.0.0.1:8000.

# Access the API
You can access the API at the following endpoint:
GET /: Retrieves the registered email, current UTC timestamp, and the GitHub repository URL.
For example, accessing http://127.0.0.1:8000/ will return a JSON response like:
{
  "email": "goodnewsagijesuefe@gmail.com",
  "timestamp": "2025-01-31T12:34:56Z",
  "github_url": "https://github.com/goodnews22r/Public-API.git"
}

# API Documentation
FastAPI automatically generates interactive API documentation. You can access it by visiting:
Swagger UI: http://127.0.0.1:8000/docs

# Deployment
This API is deployed and publicly accessible at the following URL:
Live URL: https://public-api-production-3068.up.railway.app/
The API is accessible worldwide and returns responses under 500ms.

# Example Usage
You can access the API by sending a GET request to the root endpoint. Here’s an example using curl:
curl https://public-api-production-3068.up.railway.app/

# Sample Response:
{
  "email": "goodnewsagijesuefe@gmail.com",
  "timestamp": "2025-01-31T12:34:56Z",
  "github_url": "https://github.com/goodnews22r/Public-API.git"
}

https://hng.tech/hire/python-developers
