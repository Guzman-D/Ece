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

@app.get("/exercise2")
def exercise2(a: int = 0, b: int = 0):
	return {"exercise": 2, "resultado": a + b}

@app.get("/exercise3")
def exercise3(num: int):
	return {"exercise": 3, "numero": num, "es par": num % 2 == 0} 

@app.get("/exercise4")
def exercise4():
	lista = [1, 2, 3, 4, 5]
	recorrido = [n for n in lista]
	return {"exercise": 4, "Lista": recorrido}

@app.get("/exercise5")
def exercise5(a: int, b: int):
	resultado = a * b
	return {"exercise": 5, "Resultado": resultado}

@app.get("/exercise6")
def exercise6():
        persona = {
                "nombre": "Guzman",
                "edad": 21,
                "ciudad": "Barranquilla"
        }
        return {"exercise": 6, "persona": persona}	

@app.get("/exercise7")
def exercise7():
        persona = {
                "nombre": "Guzman",
                "edad": 21,
                "ciudad": "Barranquilla"
        }
        claves = list(persona.keys())
        return {"exercise": 7, "claves": claves}
