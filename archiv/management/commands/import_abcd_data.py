import json
from django.core.serializers.json import DjangoJSONEncoder
import pandas as pd
from sqlalchemy import create_engine
from django.conf import settings
from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Event, Work
from archiv.import_utils import field_mapping
dbc = settings.LEGACY_DB_CONNECTION
db_connection_str = f"mysql+pymysql://{dbc['USER']}:{dbc['PASSWORD']}@{dbc['HOST']}/{dbc['NAME']}"
db_connection = create_engine(db_connection_str)


class Command(BaseCommand):
    help = 'Imports Legacy Data'

    def handle(self, *args, **kwargs):
        event_error = []
        query = f"SELECT * FROM {Event.get_source_table()}"
        self.stdout.write(
            self.style.NOTICE(
                f"fetching data from '{query}'"
            )
        )
        df = pd.read_sql(query, con=db_connection)
        self.stdout.write(
            self.style.NOTICE(
                f"counting '{len(df)} entries'"
            )
        )
        fm = field_mapping(Event)
        for i, row in tqdm(df.iterrows(), total=len(df)):
            try:
                item, _ = Event.objects.get_or_create(
                    order_code=row['input_Sortiercode']
                )
            except Exception as e:
                event_error.append([row['input_Sortiercode'], e])
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
        query = f"SELECT * FROM {Work.get_source_table()}"
        self.stdout.write(
            self.style.NOTICE(
                f"fetching data from '{query}'"
            )
        )
        df = pd.read_sql(query, con=db_connection)
        self.stdout.write(
            self.style.NOTICE(
                f"counting '{len(df)} entries'"
            )
        )
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

        for x in event_error:
            self.stdout.write(
                self.style.ERROR(x)
            )
        for x in work_error:
            self.stdout.write(
                self.style.ERROR(x)
            )
