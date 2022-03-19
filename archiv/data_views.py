import json
from django.http import HttpResponse
from django.views.generic import TemplateView

from archiv.models import Event


def event_calendar_data(request):
    data = []
    for x in Event.objects.exclude(not_before__isnull=True):
        item = {
            'id': x.date_written,
            'name': f"{x}",
            'startDate': f"{x.not_before}",
            'linkId': x.get_absolute_url()
        }
        data.append(item)
    var_data = f"var calendarData = {json.dumps(data, ensure_ascii=False)}"
    return HttpResponse(var_data, content_type="text/javascript")


class EventCalendarView(TemplateView):
    template_name = 'archiv/event_calendar.html'
