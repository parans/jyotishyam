from fastapi import FastAPI
from fastapi import Response
from pydantic import BaseModel
import chart_calc.mod_lagna as mod_lagna
import mod_astrodata as data
import mod_json as js
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

class BirthDetails(BaseModel):
    name: str
    dateOfBirth: str
    timeOfBirth: str
    place: str

@app.post("/birthChart/")
async def create_item(item: BirthDetails):
    mod_lagna.compute_lagnaChart()
    res = json.dumps(dict(data.charts), indent=4)
    return Response(content=res, media_type="application/json")

@app.get("/birthChart/svg")
async def chart():
    mod_lagna.compute_lagnaChart()
    js.dump_astrodata_injson()
    js.load_drawChartConfig()
    chartSVGfilename = f'{data.D1["name"]}_chart'
    res = open(f'drawCharts/chart_images/{chartSVGfilename}.svg', 'r',  encoding='utf-16').read()
    return Response(content=res, media_type="image/svg+xml")