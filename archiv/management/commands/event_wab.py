import pandas as pd

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from tqdm import tqdm
from archiv.models import Wab, Event
from archiv.import_utils import gsheet_to_df


class Command(BaseCommand):
    help = 'Links WAB to Events based on Wab-Titles'

    def handle(self, *args, **kwargs):
        sheet_id = settings.WAB_SEARCH
        df = gsheet_to_df(sheet_id)
        data = []
        for i, row in tqdm(df.iterrows(), total=len(df)):
            wab_id = f"{row['wab_rn']}".zfill(3)
            try:
                wab = Wab.objects.get(wab_id=wab_id)
            except ObjectDoesNotExist:
                data.append([wab_id, row['match_str'], 0])
                continue
            matches = Event.objects.filter(main_text__contains=row['match_str'])
            wab.rvn_wab_mentioned_in.add(*matches)
            data.append([wab_id, row['match_str'], matches.count()])
        out_df = pd.DataFrame(data, columns=['wab', 'search_str', 'matches'])
        out_df.to_csv('./media/wab_matching.csv', index=False)
