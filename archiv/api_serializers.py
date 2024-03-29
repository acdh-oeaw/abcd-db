from rest_framework import serializers
from archiv.models import Event, Work, Place, Person, Institution, Wab


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        exclude = [
            "full_text",
        ]
        depth = 1


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"
        depth = 1


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"
        depth = 1


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        depth = 1


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"
        depth = 1


class WabSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wab
        exclude = [
            "wab_xml",
        ]
        depth = 1
