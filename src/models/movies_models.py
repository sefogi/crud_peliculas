from pydantic import BaseModel as bm #BaseModel es una clase que se usa para crear los schemas
from pydantic import Field #Field es un metodo que se usa para especificar los datos que se piden en la peticion
import datetime #datetime es un modulo que se usa para trabajar con fechas y horas


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