from pydantic import BaseModel

class input_data(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float