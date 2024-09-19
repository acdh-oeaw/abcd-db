import re
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from tqdm import tqdm
from archiv.models import Event, Wab


class Command(BaseCommand):
    help = "Links WAB to Events"

    def handle(self, *args, **kwargs):
        regex = r"WAB\s?\d\d*"
        events = Event.objects.filter(full_text__contains="WAB")
        for x in tqdm(events, total=events.count()):
            wabs = set()
            wab_ids = set()
            text = x.full_text
            for m in re.findall(regex, text, re.MULTILINE):
                wab_nr = m.replace("WAB", "").strip()
                wab_id = wab_nr.zfill(3)
                wab_ids.add(wab_id)
            for w in wab_ids:
                try:
                    wab_obj = Wab.objects.get(wab_id=w)
                except ObjectDoesNotExist:
                    continue
                wabs.add(wab_obj)
            x.wab.add(*wabs)
