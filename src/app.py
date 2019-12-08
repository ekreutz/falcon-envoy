import fastapi

from routers import things

def create_app():
    app = fastapi.FastAPI()

    # Declare routers
    app.include_router(things.router)

    return app
