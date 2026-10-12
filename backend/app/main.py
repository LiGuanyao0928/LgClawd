from fastapi import FastAPI

app = FastAPI(title="Clawd Studio")


@app.get("/health")
def health() -> dict[str, str]:
    """存活检查：部署和监控用。"""
    return {"status": "ok"}
