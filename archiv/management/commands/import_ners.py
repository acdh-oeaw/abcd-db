import spacy

from django.core.management.base import BaseCommand
from tqdm import tqdm
from archiv.models import Person, Event

nlp = spacy.load("de_core_news_sm")

for x in tqdm(Event.objects.all(), total=Event.objects.all().count()):
    text = x.main_text
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == 'PER':
            pers, _ = Person.objects.get_or_create(title=ent.text)
            x.person.add(pers)