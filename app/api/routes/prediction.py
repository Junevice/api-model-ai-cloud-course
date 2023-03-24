from fastapi import APIRouter, Request

from app.models.features import Features
from app.models.prediction import Prediction

from app.services.model import Model

router = APIRouter()


@router.get("/", status_code=200)
def read_root():
    # TODO: rename this function and either point redirect on kaggle or display data stats
    return "test"


@router.post("/predict", name="predict")
async def predict(features:Features, request:Request):
    
    
    print(request.app.state.ml_models['start-model'])
    # prediction = request.app.ml_models["start-model"].predict(features)

    prediction = request.app.state.ml_models['start-model'].predict(features)

    return prediction
