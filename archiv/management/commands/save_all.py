from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Event, Person, Work


class Command(BaseCommand):
    help = "Saves all Work, Persons and Events"

    def handle(self, *args, **kwargs):
        for item in [Work, Person, Event]:
            objects = item.objects.all()
            print(f"saving {objects.count()} {item}")
            for x in tqdm(objects, total=objects.count()):
                x.save()
        print("Done saving")
