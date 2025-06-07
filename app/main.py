from fastapi import FastAPI
from .routes import generate

app = FastAPI(
    title="Link2Resume",
    description="An API that converts your online profile to website and resume",
    version="0.0.1"
)

app.include_router(generate.router, prefix="/api")