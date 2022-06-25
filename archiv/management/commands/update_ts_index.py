from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Event


class Command(BaseCommand):
    help = 'Updates Typesense Index'

    def handle(self, *args, **kwargs):
        Event.ts_recreate_schema()
        items = Event.objects.all()
        records = []
        for x in tqdm(items, total=items.count()):
            records.append(x.ts_make_document())
        Event.ts_update_index(records)
        print("Done Indexing, happy searching")
