from fastapi import FastAPI
from .core.settings import settings
from .routers.security import router as security_router 

app = FastAPI(title="My Azure API", version="0.1.0")

@app.get("/healthz")
def healthz():
    return {"status": "ok", "message": "api running"}

# Mount routers here
app.include_router(security_router)
