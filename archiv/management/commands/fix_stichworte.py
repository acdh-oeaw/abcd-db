from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Event
from archiv.import_utils import gsheet_to_df


class Command(BaseCommand):
    help = 'Imports text_Stichworte Data'

    def handle(self, *args, **kwargs):
        sheet_id = settings.LEGACY_DB_SHEET_ID
        self.stdout.write(f"fetching data from {sheet_id}")
        df = gsheet_to_df(sheet_id)
        df = df.dropna(subset=['text_Stichworte', 'input_Sortiercode'])
        for i, row in tqdm(df.iterrows(), total=len(df)):
            try:
                event = Event.objects.get(id=row['input_Sortiercode'])
            except ObjectDoesNotExist:
                continue
            stichwort = row['text_Stichworte']
            event.key_word = stichwort
            event.save()
        self.stdout.write("done")
