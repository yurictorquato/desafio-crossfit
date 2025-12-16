from fastapi import FastAPI

from app.routers import api_router

app = FastAPI(title="Crossfit Center API")

app.include_router(api_router)
