from pydantic import BaseModel

class CatDogResponse(BaseModel):
    probs : list = []
    best_prob : float = -1.0
    predicted_id : int = -1
    predicted_class : str = ""
    predictor_name : str = ""