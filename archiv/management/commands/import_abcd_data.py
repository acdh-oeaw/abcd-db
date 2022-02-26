import json
from django.core.serializers.json import DjangoJSONEncoder
import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Event, Work
from archiv.import_utils import field_mapping
from archiv.import_utils import gsheet_to_df


class Command(BaseCommand):
    help = 'Imports Legacy Data'

    def handle(self, *args, **kwargs):
        sheet_id = settings.LEGACY_DB_SHEET_ID
        event_error = []
        self.stdout.write(f"fetching data from {sheet_id}")
        df = gsheet_to_df(sheet_id)
        fm = field_mapping(Event)
        for i, row in tqdm(df.iterrows(), total=len(df)):
            try:
                item, _ = Event.objects.get_or_create(
                    id=row['input_Sortiercode']
                )
            except Exception as e:
                event_error.append([row['input_Sortiercode'], e])
                continue
            for x in fm.keys():
                if isinstance(row[x], str):
                    setattr(
                        item,
                        fm[x],
                        row[x]
                    )
            row_data = f"{json.dumps(row.to_dict(), cls=DjangoJSONEncoder)}"
            item.orig_data_csv = row_data
            try:
                item.save()
            except Exception as e:
                event_error.append([row['input_Sortiercode'], e])

        self.stdout.write(
            self.style.SUCCESS(
                "DONE with Events"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                "#######################"
            )
        )
        work_error = []
        sheet_id = settings.LEGACY_DB_LIT_SHEET_ID
        self.stdout.write(f"fetching data from {sheet_id}")
        df = gsheet_to_df(sheet_id)
        fm = field_mapping(Work)
        for i, row in tqdm(df.iterrows(), total=len(df)):
            try:
                item, _ = Work.objects.get_or_create(
                    order_code=row['input_Nummer']
                )
            except Exception as e:
                work_error.append([row['input_Nummer'], e])
                continue
            for x in fm.keys():
                setattr(
                    item,
                    fm[x],
                    row[x]
                )
            row_data = f"{json.dumps(row.to_dict(), cls=DjangoJSONEncoder)}"
            item.orig_data_csv = row_data
            try:
                item.save()
            except Exception as e:
                work_error.append([row['input_Nummer'], e])
        self.stdout.write(
            self.style.SUCCESS(
                "DONE with Works"
            )
        )
        df = pd.DataFrame(event_error)
        df.to_csv('./media/event_error.csv')
        df = pd.DataFrame(work_error)
        df.to_csv('./media/work_error.csv')
        for x in event_error:
            self.stdout.write(
                self.style.ERROR(x)
            )
        for x in work_error:
            self.stdout.write(
                self.style.ERROR(x)
            )
