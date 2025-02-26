from typing import Optional, List
from fastapi import Path, Query, APIRouter
from fastapi.responses import JSONResponse
from src.models.movies_models import Movie, MovieCreate, MovieUpdate #importamos los schemas de las peliculas

movies: List[Movie] = [] #creamos una lista de peliculas

movie_router = APIRouter() #creamos un router




@movie_router.get("/", tags=["Movies"])
def get_movies() -> List[Movie]:#se especifica que la funcion devuelve una lista de peliculas
    return [movie.model_dump() for movie in movies]#se devuelve una lista de 

@movie_router.get("/{id}", tags=["Movies"])
def get_movie(id: int = Path(gt=0)) -> Movie | dict: #se especifica que la funcion devuelve una pelicula o un diccionario
    for movie in movies:
        if movie.id == id:
            return movie
    return {}


@movie_router.get("/by_genre", tags=["Movies"])#para que sea query se coloca la ruta con dos barras
def get_movie_by_genre(genre: str = Query(min_length=5, max_length=20), ) -> Movie | dict: #para que sea una peticion query de coloca el nombre de la variable y el tipo de dato dentro de la funcion
    for movie in movies:
        if movie.genre == genre:
            return movie.model_dump()
    return {} #se devuelve un diccionario vacio si no se encuentra la pelicula


@movie_router.post("/", tags=["Movies"])
def create_movie(movie : MovieCreate)-> List[Movie]:
    movies.append(movie)#solo regitro el objeto en la lista
    return [movie.model_dump() for movie in movies]
    
@movie_router.put("/{id}", tags=["Movies"])
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
@movie_router.delete("/{id}", tags=["Movies"])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
        return [movie.model_dump() for movie in movies]
    
    
    