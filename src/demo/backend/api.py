from fastapi import APIRouter, HTTPException, Header

API_VERSION = "v1"

def make_api_router(settings):
    app = APIRouter()


    @app.get("/test")
    def test():
        return "Test"

    return app
