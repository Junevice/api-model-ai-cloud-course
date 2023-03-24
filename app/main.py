from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import (API_PREFIX, APP_NAME, APP_VERSION, IS_DEBUG)

from app.core.event_handlers import lifespan

def get_app() -> FastAPI:
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG, lifespan=lifespan)
    fast_app.include_router(api_router, prefix=API_PREFIX)
    

    return fast_app



app = get_app()
