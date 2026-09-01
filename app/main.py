from fastapi import FastAPI

app = FastAPI(title="Kubernetes Production Deployment")


@app.get("/")
def root():
    return {
        "message": "Kubernetes Production Deployment",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }