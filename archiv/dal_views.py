# generated by appcreator
from django.db.models import Q
from dal import autocomplete
from .models import Event, Work, Person, Place, Institution, Wab


class PersonAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(
                Q(title__icontains=self.q)
                | Q(gnd_gnd_id=self.q)
                | Q(gnd_pref_name=self.q)
            )
        return qs


class PlaceAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Place.objects.all()

        if self.q:
            qs = qs.filter(Q(title__icontains=self.q))
        return qs


class WabAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Wab.objects.all()

        if self.q:
            qs = qs.filter(Q(title__icontains=self.q))
        return qs


class InstitutionAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Institution.objects.all()

        if self.q:
            qs = qs.filter(Q(title__icontains=self.q))
        return qs


class EventAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Event.objects.all()

        if self.q:
            qs = qs.filter(Q(id__icontains=self.q) | Q(full_text__icontains=self.q))
        return qs


class WorkAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Work.objects.all()

        if self.q:
            qs = qs.filter(
                Q(order_code__icontains=self.q) | Q(full_quote__icontains=self.q)
            )
        return qs
