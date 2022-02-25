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
            lit_main_text = event.main_text
            lit_notes_lit = event.notes_lit
            lit_notes_img = event.notes_img
            lit_notes_facs = event.notes_facs
            lit_notes_archive = event.notes_archive
            lit_notes_text = event.notes_text
            lit_note = event.note

            number = []
            number.append(re.findall('([0-9]+)/[0-9]+', lit_main_text))
            number.append(re.findall('([0-9]+)/[0-9]+', lit_notes_lit))
            number.append(re.findall('([0-9]+)/[0-9]+', lit_notes_img))
            number.append(re.findall('([0-9]+)/[0-9]+', lit_notes_facs))
            number.append(re.findall('([0-9]+)/[0-9]+', lit_notes_archive))
            number.append(re.findall('([0-9]+)/[0-9]+', lit_notes_text))
            number.append(re.findall('([0-9]+)/[0-9]+', lit_note))

            if len(number) != 0:

                for number_list in number:

                    for literature in number_list:

                        number_int = int(literature)
                        lit_string = 'Lit.' + ('%04d' % number_int)

                        try:
                            related_work = Work.objects.get(order_code=lit_string)
                        except ObjectDoesNotExist:
                            failed = [event.id, lit_string]
                            failed.append(miss_matches)
                            continue

                        event.work.add(related_work)
        df = pd.DataFrame(miss_matches)
        df.to_csv('./media/miss_matches.csv')
