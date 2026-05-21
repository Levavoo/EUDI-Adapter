from fastapi import FastAPI

app = FastAPI(
    title="EUDI Relying Party Integration Bus",
    version="0.1.0",
    description=(
        "Prototype for translating business identity-check requirements "
        "into privacy-preserving EUDI Wallet verification requests."
    ),
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": "EUDI Relying Party Integration Bus",
        "status": "running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}