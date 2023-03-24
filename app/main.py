from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import (API_PREFIX, APP_NAME, APP_VERSION,
                             IS_DEBUG)


def get_app() -> FastAPI:
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)
    fast_app.include_router(api_router, prefix=API_PREFIX)
    # TODO : Add event handlers
    return fast_app


app = get_app()
