from fastapi import FastAPI

from src.example.routes import router as example_router


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router=example_router, prefix="/example")
    return app
