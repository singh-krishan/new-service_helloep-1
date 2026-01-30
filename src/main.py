"""
A Python microservice
"""
from fastapi import FastAPI
import os

app = FastAPI(
    title="new-service_helloep-1",
    description="A Python microservice",
    version="0.1.0"
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to new-service_helloep-1",
        "version": "0.1.0"
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "new-service_helloep-1"
    }


@app.get("/hello")
async def hello():
    """Custom hello endpoint."""
    return {
        "message": "hello, welcome to my IDP"
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8002"))
    uvicorn.run(app, host="0.0.0.0", port=port)
