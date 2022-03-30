import django_filters

from . models import (
    SkosTechnicalCollection,
    SkosConcept,
    SkosCollection,
)


class SkosTechnicalCollectionListFilter(django_filters.FilterSet):
    pref_label = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    class Meta:
        model = SkosTechnicalCollection
        fields = [
            'pref_label'
        ]


class SkosCollectionListFilter(django_filters.FilterSet):
    pref_label = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    class Meta:
        model = SkosCollection
        fields = [
            'pref_label'
        ]


class SkosConceptListFilter(django_filters.FilterSet):
    pref_label = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    class Meta:
        model = SkosConcept
        fields = [
            'pref_label',
            'collection',
        ]
