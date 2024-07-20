from typing import List
from ninja import NinjaAPI
from birthdays.models import Cat, Dog
from birthdays.schema import CatSchema, DogSchema, NotFoundSchema

api = NinjaAPI()

@api.get("/dogs", response=List[DogSchema])
def dogs(request):
    return Dog.objects.all()

@api.get("/cats", response=List[CatSchema])
def cats(request):
    return Cat.objects.all()

@api.get("/dogs/{dog_id}", response={200: DogSchema, 404: NotFoundSchema})
def dog(request, dog_id: int):
    try:
        track = Dog.objects.get(pk=dog_id)
        return 200, track
    except Dog.DoesNotExist as e:
        return 404, {"message": f"Dog with an ID of '{dog_id}' does not exist"}
    
@api.get("/cats/{cat_id}", response={200: CatSchema, 404: NotFoundSchema})
def dog(request, cat_id: int):
    try:
        track = Cat.objects.get(pk=cat_id)
        return 200, track
    except Cat.DoesNotExist as e:
        return 404, {"message": f"Cat with an ID of '{cat_id}' does not exist"}


