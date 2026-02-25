from fastapi import FastAPI
from pydantic import BaseModel
import json
app=FastAPI()
@app.get("/")
def initialEndpoint():
	return {"message":"Hola mundo"}

@app.get("/exercise1")
def exercise1():
	nombre="Guzman"
	return{"exercise":1,"value":nombre}
