from pydantic import BaseModel
from typing import List


class IrisPredict(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisTrain(BaseModel):
    data: List[List[float]]
    targets: List[float]