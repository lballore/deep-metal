import logging
import os
import sys

from gunicorn.app.base import BaseApplication

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from api import API_VERSION, make_api_router
from config import Settings


class Application(BaseApplication):
    def __init__(self, app, options={}):
        self.options = options
        if "worker_class" not in self.options:
            self.options["worker_class"] = "uvicorn.workers.UvicornWorker"
        if "workers" not in self.options:
            self.options["workers"] = 1
        self.application = app
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def run_application(app, options={}):
    Application(app, options).run()


def make_app(settings):
    app = FastAPI(
        title = "DeepMetal API",
        description = "AI-powered heavy metal lyrics generator.",
        version = "0.0.1"
    )
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    api_router = make_api_router(settings)
    app.include_router(api_router, prefix=f"/api/{API_VERSION}")

    @app.get("/healthcheck")
    def healthcheck():
        return "OK"

    app.mount(
        "/static",
        StaticFiles(directory=(settings.STATIC_FILES_ROOT)),
        name="static",
    )

    @app.get("/{_path:path}", include_in_schema=False)
    def root(_path: str):
        return FileResponse(os.path.join(settings.STATIC_FILES_ROOT, "index.html"))

    return app


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
        datefmt="[%Y-%m-%d %H:%M:%S %z]"
    )

    settings = Settings()
    app = make_app(settings)

    run_application(app, {"bind": "0.0.0.0:8080"})


