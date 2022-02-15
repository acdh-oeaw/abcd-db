import spacy

from django.core.management.base import BaseCommand
from tqdm import tqdm
from archiv.models import Place, Institution, Person, Event


class Command(BaseCommand):
    help = 'NER things'

    def handle(self, *args, **kwargs):

        for x in [Person, Place, Institution]:
            x.objects.all().delete()

        nlp = spacy.load("de_core_news_lg")

        for x in tqdm(Event.objects.all(), total=Event.objects.all().count()):
            text = x.main_text
            doc = nlp(text)
            for ent in doc.ents:
                if ent.label_ == 'PER':
                    if ' ' in ent.text:
                        pers, _ = Person.objects.get_or_create(title=ent.text)
                        x.person.add(pers)
                if ent.label_ == 'LOC':
                    loc, _ = Place.objects.get_or_create(title=ent.text)
                    x.place.add(loc)
