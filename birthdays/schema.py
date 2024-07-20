from datetime import date
from ninja import Schema

class CatSchema(Schema): 
    name: str
    birthday: date

class DogSchema(Schema): 
    name: str
    birthday: date

class NotFoundSchema(Schema): 
    message: str