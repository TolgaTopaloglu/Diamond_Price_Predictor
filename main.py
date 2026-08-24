import pandas as pd
import pickle
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app= FastAPI()

templates= Jinja2Templates(directory="templates")

with open("DiamondRegression (1).pkl", "rb") as file:
    model= pickle.load(file)

class DiamondPriceFeature(BaseModel):
    carat: float
    cut: str
    color: str
    clarity: str
    depth: float
    table:float
    x: float
    y: float
    z: float

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(features: DiamondPriceFeature):

    input_data = pd.DataFrame([features.model_dump()])

    prediction = model.predict(input_data)

    return {"prediction": float(prediction[0])}

