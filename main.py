from typing import Union #Union es un metodo que se usa para especificar que un parametro puede ser de varios tipos de datos
from fastapi import FastAPI, Body #Body es un metodo que se usa para recibir datos en el cuerpo de la peticion
from pydantic import BaseModel as bm #BaseModel es una clase que se usa para crear los schemas
from pydantic import Field #Field es un metodo que se usa para especificar los datos que se piden en la peticion
from typing import Optional, List #Optional es un metodo que se usa para especificar que un parametro es opcional y list es un metodo que se usa para especificar que un parametro es una lista
import datetime #datetime es un modulo que se usa para trabajar con fechas y horas

app = FastAPI()

class Movie(bm):#creamos el schema de la pelicula
    id: int
    title: str
    year: int
    genre: str
    category: str
    director: str
    rating: float
    
class MovieCreate(bm):
    id: int = Field(default="2")
    title: str = Field(min_length=5, max_length=15, default="My Movie")#default es un metodo que se usa para especificar un valor por defecto
    year: int = Field(le=datetime.date.today().year, ge=1900, default="2024")
    genre: str= Field(min_length=5, max_length=15, default="Action")
    category: str= Field(min_length=1, max_length=15, default="A")
    director: str = Field(min_length=5, max_length=15, default="John Doe")
    rating: float= Field(le=10.0, ge=0.0, default=5.0)
# para valores numericos usamos "ge" para especificar que el valor debe ser mayor o igual a un valor y "le" para especificar que el valor debe ser menor o igual a un valor tambien se usan "eq" para especificar que el valor debe ser igual a un valor y "ne" para especificar que el valor debe ser diferente a un valor

class MovieUpdate(bm):
    title: str
    year: int
    genre: str
    category: str
    director: str
    rating: float

movies: List[Movie] = [] #creamos una lista de peliculas
  

app.title = "API de prueba" # titulo de la API
app.version = "0.0.1.1" # version de la API

@app.get("/", tags=["Home"]) # los tags se usan para indicar a que grupo pertenece la ruta
def home() :
    return "hola capullo"

@app.get("/movies", tags=["Movies"])
def get_movies() -> List[Movie]:#se especifica que la funcion devuelve una lista de peliculas
    return [movie.model_dump() for movie in movies]#se devuelve una lista de 

@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int) -> Optional[Movie]:
    for movie in movies:
        if movie.id == id:
            return movie
    return None


@app.get("/movies/", tags=["Movies"])
def get_movie_by_genre(genre: str, year: int) -> Movie | None:
    for movie in movies:
        if movie.genre == genre and movie.year == year:
            return movie
    return None
# @app.get("/movies/", tags=["Movies"])#para que sea query se coloca la ruta con dos barras
# def get_movie_by_genre(genre: str, year: int) ->Movie:#para que sea una peticion query de coloca el nombre de la variable y el tipo de dato dentro de la funcion
#     for movie in movies:
#         if movie['genre'] == genre and movie['year'] == year:
#             return movie.model_dump()
#     return []

@app.post("/movies/", tags=["Movies"])
def create_movie(movie : MovieCreate)-> List[Movie]:
    movies.append(movie)#solo regitro el objeto en la lista
    return [movie.model_dump() for movie in movies]
    
@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:
    for item in movies:
        if item.id == id:
            item.title = movie.title
            item.year = movie.year
            item.genre = movie.genre
            item.category = movie.category
            item.director = movie.director
            item.rating = movie.rating
            break
    return [movie.model_dump() for movie in movies]
@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
        return [movie.model_dump() for movie in movies]
    
    
    