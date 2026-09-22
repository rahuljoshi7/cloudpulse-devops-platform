from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(
    title="CloudPulse Demo Application",
    description="Sample application managed by the CloudPulse platform",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "application": "CloudPulse Demo Application",
        "message": "Application is running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/api/info")
def info():
    return {
        "application": "cloudpulse-demo-app",
        "version": "1.0.0",
        "environment": "development",
        "managed_by": "CloudPulse",
    }