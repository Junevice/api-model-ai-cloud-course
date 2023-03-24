from fastapi import APIRouter

from app.models.features import Features

router = APIRouter()


@router.get("/", status_code=200)
def read_root():
    # TODO: rename this function and either point redirect on kaggle or display data stats
    return "test"


@router.post("/predict", name="predict")
async def predict(
        features: Features):
    model = ""  # TODO: access your model instance
    prediction = model.predict()  # TODO : complete prediction
    return prediction
