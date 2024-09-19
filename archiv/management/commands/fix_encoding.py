from django.core.management.base import BaseCommand
from django.conf import settings
from tqdm import tqdm
from archiv.models import Event
from archiv.import_utils import gsheet_to_df


class Command(BaseCommand):
    help = "Fix wrong encoding of latin chars"

    def handle(self, *args, **kwargs):
        fields = Event.search_field_names()
        df = gsheet_to_df(settings.SPECIAL_CHARS_SHEET_ID)
        for x in tqdm(Event.objects.filter(), total=Event.objects.all().count()):
            for f in fields:
                old = None
                old = getattr(x, f)
                if old is not None:
                    for i, row in df.iterrows():
                        old = old.replace(row["from"], row["to"])
                setattr(x, f, old)
            x.save()
        print("done")
