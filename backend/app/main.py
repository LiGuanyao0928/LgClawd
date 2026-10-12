from fastapi import FastAPI

app = FastAPI(title="LgClawd")


@app.get("/health")
def health() -> dict[str, str]:
    """存活检查：部署和监控用。"""
    return {"status": "ok"}
