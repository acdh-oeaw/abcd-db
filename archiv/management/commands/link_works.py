import re
import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from tqdm import tqdm
from archiv.models import Event, Work


class Command(BaseCommand):
    help = 'Links works to Events'

    def handle(self, *args, **kwargs):
        miss_matches = []
        all_events = Event.objects.all()
        for event in tqdm(all_events, total=len(all_events)):
            try:
                number = re.findall('([0-9]+)/[0-9]+', event.full_text)
            except TypeError:
                continue
            works = []
            for literature in set(number):
                number_int = int(literature)
                lit_string = 'Lit.' + ('%04d' % number_int)
                try:
                    related_work = Work.objects.get(order_code=lit_string)
                except ObjectDoesNotExist:
                    failed = [event.id, lit_string]
                    miss_matches.append(failed)
                    continue
                works.append(related_work)
            event.work.set(works)
        df = pd.DataFrame(miss_matches)
        df.to_csv('./media/miss_matches.csv')
