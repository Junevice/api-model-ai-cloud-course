from typing import Callable

from fastapi import FastAPI
from loguru import logger

from contextlib import asynccontextmanager

from app.services.model import Model


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    app.state.ml_models = {}
    app.state.ml_models['start-model'] = Model()
    print('runned')
    yield
    # Clean up the ML models and release the resources
    app.state.ml_models.clear()