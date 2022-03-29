from django.conf import settings
from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Event
from archiv.import_utils import gsheet_to_df

from vocabs.models import SkosCollection, SkosConcept, SkosTechnicalCollection


class Command(BaseCommand):
    help = 'Imports Keywords'

    def handle(self, *args, **kwargs):
        tech_col, _ = SkosTechnicalCollection.objects.get_or_create(
            pref_label='event__key_word'
        )
        klaeren, _ = SkosCollection.objects.get_or_create(
            pref_label="klären"
        )
        wab, _ = SkosCollection.objects.get_or_create(
            pref_label="WAB"
        )
        mus_hs, _ = SkosCollection.objects.get_or_create(
            pref_label="Mus.Hs."
        )
        detail, _ = SkosCollection.objects.get_or_create(
            pref_label="detaillieren"
        )
        jahreszahl, _ = SkosCollection.objects.get_or_create(
            pref_label=". Datum"
        )
        schlagwort, _ = SkosCollection.objects.get_or_create(
            pref_label="Schlagwort"
        )
        sheet_id = settings.LEGACY_DB_SHEET_ID
        self.stdout.write(f"fetching data from {sheet_id}")
        df = gsheet_to_df(sheet_id)
        filtered_df = df[df['text_Stichworte'].notnull()]
        for i, row in tqdm(filtered_df.iterrows(), total=len(filtered_df)):
            try:
                event = Event.objects.get(id=row['input_Sortiercode'])
            except Exception:
                continue
            words = row['text_Stichworte']
            for x in words.split(', '):
                if len(x) > 3:
                    concept, _ = SkosConcept.objects.get_or_create(
                        pref_label=x[:249],
                    )
                    concept.tech_collection.add(tech_col)
                    if 'WAB' in x:
                        concept.collection = wab
                    elif 'klären' in x:
                        concept.collection = klaeren
                    elif 'Mus.Hs.' in x:
                        concept.collection = mus_hs
                    elif 'detaillieren' in x:
                        concept.collection = detail
                    elif x[0] == '.':
                        concept.collection = jahreszahl
                    else:
                        concept.collection = schlagwort
                    concept.save()
                    event.key_word.add(concept)
