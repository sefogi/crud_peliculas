from typing import Union
from fastapi import FastAPI, Body #Body es un metodo que se usa para recibir datos en el cuerpo de la peticion
from pydantic import BaseModel

app = FastAPI()

movies = [#bd de peliculas
  {
    "id": "1",
    "title": "Inception",
    "year": 2010,
    "genre": "Sci-Fi", 
    "category": "Movie",
    "director": "Christopher Nolan",
    "rating": 8.8
  },
  {
    "id": "2",
    "title": "The Shawshank Redemption",
    "year": 1994,
    "genre": "Drama",
    "category": "Movie",
    "director": "Frank Darabont",
    "rating": 9.3
  },
  {
    "id": "3", 
    "title": "Breaking Bad",
    "year": 2008,
    "genre":"Crime", 
    "category": "TV Show",
    "director": "Vince Gilligan",
    "rating": 9.5
  },
  {
    "id": "4", 
    "title": "Parasite",
    "year": 2019,
    "genre":  "Thriller",
    "category":"Movie",
    "director": "Bong Joon-ho",
    "rating": 8.6
  },
  {
    "id": "5", 
    "title": "Stranger Things",
    "year": 2016,
    "genre": "Fantasy", 
    "category": "TV Show",
    "director": "The Duffer Brothers",
    "rating": 8.7
  },
  {
    "id": "6", 
    "title": "The Matrix",
    "year": 1999,
    "genre": "Action", 
    "category": "Movie",
    "director": "The Wachowskis",
    "rating": 8.7
  },
  {
    "id": "7", 
    "title": "The Dark Knight",
    "year": 2008,
    "genre": "Action",
    "category": "Movie",
    "director": "Christopher Nolan",
    "rating": 9.0
  },
  {
    "id": "8",
    "title": "Game of Thrones",
    "year": 2011,
    "genre": "Action", 
    "category": "TV Show",
    "director": "David Benioff, D.B. Weiss",
    "rating": 9.2
  },
  {
    "id": "9", 
    "title": "Pulp Fiction",
    "year": 1994,
    "genre": "Crime",
    "category": "Movie",
    "director": "Quentin Tarantino",
    "rating": 8.9
  },
  {
    "id": "10",
    "title": "The Office",
    "year": 2005,
    "genre": "Comedy",
    "category": "TV Show",
    "director": "Greg Daniels",
    "rating": 9.0
  }
]

app.title = "API de prueba" # titulo de la API
app.version = "0.0.1.1" # version de la API

@app.get("/", tags=["Home"]) # los tags se usan para indicar a que grupo pertenece la ruta
def home():
    return "hola capullo"

@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies

@app.get("/movies/{id}", tags=["Movies"])# el id es un parametro que se pide en la ruta
def get_movie(id: str):#aqui se especifica que el id es un string
    for movie in movies:#creamos un bucle para recorrer la lista de peliculas
        if movie['id'] == id:#si el id de la pelicula es igual al id que se pide en la ruta
            return movie
    return []

@app.get("/movies/", tags=["Movies"])#para que sea query se coloca la ruta con dos barras
def get_movie_by_genre(genre: str, year: int):#para que sea una peticion query de coloca el nombre de la variable y el tipo de dato dentro de la funcion
    result = []
    for movie in movies:
        if movie['genre'] == genre and movie['year'] == year:
            result.append(movie)
    
    return result

@app.post("/movies/", tags=["Movies"])
def create_movie(id: str = Body(), title: str = Body(), year: int= Body(), genre: str= Body(), category: str= Body(), director: str= Body(), rating: float= Body()):
    movies.append({
        "id": id,
        "title": title,
        "year": year,
        "genre": genre,
        "category": category,
        "director": director,
        "rating": rating
    })
    
    return movies
    
@app.put("/movies/{id}", tags=["Movies"])
def update_movie( id: str , title: str = Body(), year: int= Body(), genre: str= Body(), category: str= Body(), director: str= Body(), rating: float= Body()):
    for movie in movies:
        if movie["id"]==id:
            movie["title"] = title
            movie["year"] = year
            movie["genre"] = genre
            movie["category"] = category
            movie["director"] = director
            movie["rating"] = rating
        return movies
    
@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: str):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
        return movies
    
    
    