import django_filters.rest_framework
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from archiv.models import Event, Work, Place, Person, Institution, Wab
from archiv.api_serializers import (
    EventSerializer,
    WorkSerializer,
    PersonSerializer,
    PlaceSerializer,
    InstitutionSerializer,
    WabSerializer,
)
from archiv.filters import EventListFilter


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().distinct()
    serializer_class = EventSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_class = EventListFilter


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all().distinct()
    serializer_class = WorkSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter,
    ]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().distinct()
    serializer_class = PersonSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter,
    ]


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all().distinct()
    serializer_class = PlaceSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter,
    ]


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all().distinct()
    serializer_class = InstitutionSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter,
    ]


class WabViewSet(viewsets.ModelViewSet):
    queryset = Wab.objects.all().distinct()
    serializer_class = WabSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter,
    ]
