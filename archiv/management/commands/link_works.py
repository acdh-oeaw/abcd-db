
from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Event, Work
import re


class Command(BaseCommand):
    help = 'Links works to Events'

    def handle(self, *args, **kwargs):
        import re

        dict_lit = {}

        all_events = Event.objects.all()

        for event in all_events:
        
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
                        except: # DoesNotExist:
                            continue

                        event.work.add(related_work)

                        if event.id in dict_lit:
                            if lit_string not in dict_lit[event.id]:
                                dict_lit[event.id].append(lit_string)

                        else:
                            dict_lit[event.id] = [lit_string]