import spacy

from django.core.management.base import BaseCommand
from django.utils.html import strip_tags
from tqdm import tqdm
from archiv.models import Place, Institution, Person, Event

PERS_TO_EXLUDE = [
    'Anton Bruckner',
    'Anton Bruckners',
]


class Command(BaseCommand):
    help = 'NER things'

    def handle(self, *args, **kwargs):

        for x in [Person, Place, Institution]:
            x.objects.all().delete()

        nlp = spacy.load("de_core_news_lg")

        for x in tqdm(Event.objects.all(), total=Event.objects.all().count()):
            orig_text = x.main_text
            text = strip_tags(orig_text).replace('\n', ' ')
            doc = nlp(text)
            for ent in doc.ents:
                if not ent.text[0].isalpha():
                    continue
                if ent.text[0].islower():
                    continue
                if ent.label_ == 'PER':
                    if ' ' in ent.text and ent.text not in PERS_TO_EXLUDE and len(ent.text) > 7:
                        try:
                            pers, _ = Person.objects.get_or_create(title=ent.text)
                        except Exception as e:
                            print(e)
                            print(ent.text)
                            continue
                        x.person.add(pers)
                # elif ent.label_ == 'LOC':
                #     if len(ent.text) > 3:
                #         try:
                #             loc, _ = Place.objects.get_or_create(title=ent.text)
                #         except Exception as e:
                #             print(e)
                #             print(ent.text)
                #             continue
                #         x.place.add(loc)
                # else:
                #     pass
