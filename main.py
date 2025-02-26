from typing import Union #Union es un metodo que se usa para especificar que un parametro puede ser de varios tipos de datos
from fastapi import FastAPI, Body, Path, Query #Body es un metodo que se usa para recibir datos en el cuerpo de la peticion
from typing import Optional, List #Optional es un metodo que se usa para especificar que un parametro es opcional y list es un metodo que se usa para especificar que un parametro es una lista
import datetime #datetime es un modulo que se usa para trabajar con fechas y horas
from src.routers.movie_router import movie_router #importamos el router de las peliculas


app = FastAPI()





  

app.title = "API de prueba" # titulo de la API
app.version = "0.0.1.1" # version de la API

@app.get("/", tags=["Home"]) # los tags se usan para indicar a que grupo pertenece la ruta
def home() :
    return "hola capullo"

app.include_router(prefix= '/movies', router= movie_router) #incluimos el router de las peliculas en la aplicacion

