import json

from django.conf import settings
from django.core.management.base import BaseCommand

from birthdays.models import Cat, Dog

class Command(BaseCommand):
    help = 'Load Cat and Dog Birthdays from JSON file(s)'

    def handle(self, *args, **kwargs):
        # set the path to cat_birthdays.json and dog_birthdays.json
        cat_birthdays_json = settings.BASE_DIR / 'data' / 'cat_birthdays.json'
        dog_birthdays_json = settings.BASE_DIR / 'data' / 'dog_birthdays.json'
        assert cat_birthdays_json.exists()
        assert dog_birthdays_json.exists()

        # load cat_birthdays.json
        with open(cat_birthdays_json, 'r') as f:
            cat_birthday_data = json.load(f)

        # load dog_birthdays.json
        with open(dog_birthdays_json, 'r') as f:
            dog_birthday_data = json.load(f)
        
        # convert list of dictionaries to list of Cat and Dog models, and bulk_create
        cat_birthdays = [Cat(**cat) for cat in cat_birthday_data]
        dog_birthdays = [Dog(**dog) for dog in dog_birthday_data]

        Cat.objects.bulk_create(cat_birthdays)
        Dog.objects.bulk_create(dog_birthdays)