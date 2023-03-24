import joblib
from app.core.config import DEFAULT_MODEL_PATH

class Model:

    def __init__(self):
        self.model = joblib.load(DEFAULT_MODEL_PATH, mmap_mode=None)

    def predict(self, features) -> dict:
        
        predicted = self.model.predict([[feature[1] for feature in features]])
        confidence_score = self.model.predict_proba([[feature[1] for feature in features]])

        return [bool(predicted[0]), confidence_score]


