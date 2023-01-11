from datetime import date
from archiv.import_utils import gsheet_to_df
from django.core.management.base import BaseCommand
from archiv.models import Event, Person


class Command(BaseCommand):
    help = 'Links Persons to Events'

    def handle(self, *args, **kwargs):
        sheet_id = "1o0eUACXdLRu0jz_NGDsj3A3iIHeaQeEPGvXn3THktoE"
        today = date.today()
        df = gsheet_to_df(sheet_id)
        for g, ndf in df.groupby('entity_id'):
            entity = Person.objects.get(id=g)
            event_ids = ndf['event_id'].values
            events = Event.objects.filter(id__in=event_ids).distinct()
            before = entity.rvn_person_mentioned_in.all().count()
            entity.rvn_person_mentioned_in.add(*events)
            after = entity.rvn_person_mentioned_in.all().count()
            msg = f'\nVerlinkung ergänzt via Script am {today.strftime("%d.%m.%Y")}'
            entity.status = f"{entity.status}{msg}"
            entity.save()
            print(g, before, after)
        print("done")
