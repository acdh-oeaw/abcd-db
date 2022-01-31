# generated by appcreator
import django_filters

from dal import autocomplete
from django import forms
from vocabs.models import SkosConcept

from . models import (
    Event,
    Reference,
    Work
)

NUMBER_LOOKUP_CHOICES = [
    ('exact', 'Equals'),
    ('gt', 'Greater than'),
    ('lt', 'Less than')
]

CHAR_LOOKUP_CHOICES = [
    ('icontains', 'Contains'),
    ('iexact', 'Equals'),
    ('istartswith', 'Starts with'),
    ('iendswith', 'Ends with')
]


class EventListFilter(django_filters.FilterSet):
    legacy_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('legacy_id').help_text,
        label=Event._meta.get_field('legacy_id').verbose_name
    )
    date_written = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('date_written').help_text,
        label=Event._meta.get_field('date_written').verbose_name
    )
    main_text = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('main_text').help_text,
        label=Event._meta.get_field('main_text').verbose_name
    )
    notes_lit = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('notes_lit').help_text,
        label=Event._meta.get_field('notes_lit').verbose_name
    )
    notes_img = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('notes_img').help_text,
        label=Event._meta.get_field('notes_img').verbose_name
    )
    notes_facs = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('notes_facs').help_text,
        label=Event._meta.get_field('notes_facs').verbose_name
    )
    notes_archive = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('notes_archive').help_text,
        label=Event._meta.get_field('notes_archive').verbose_name
    )
    notes_text = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('notes_text').help_text,
        label=Event._meta.get_field('notes_text').verbose_name
    )
    key_word = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            tech_collection__pref_label="event__key_word"
        ),
        help_text=Event._meta.get_field('key_word').help_text,
        label=Event._meta.get_field('key_word').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/concept/event__key_word",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    note = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('note').help_text,
        label=Event._meta.get_field('note').verbose_name
    )
    reference = django_filters.ModelMultipleChoiceFilter(
        queryset=Reference.objects.all(),
        help_text=Event._meta.get_field('reference').help_text,
        label=Event._meta.get_field('reference').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:reference-autocomplete",
        )
    )

    class Meta:
        model = Event
        fields = [
            'id',
            'legacy_id',
            'order_code',
            'date_written',
            'not_before',
            'not_after',
            'main_text',
            'notes_lit',
            'notes_img',
            'notes_facs',
            'notes_archive',
            'notes_text',
            'key_word',
            'note',
            'reference',
            
        ]


class ReferenceListFilter(django_filters.FilterSet):
    legacy_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Reference._meta.get_field('legacy_id').help_text,
        label=Reference._meta.get_field('legacy_id').verbose_name
    )
    work = django_filters.ModelMultipleChoiceFilter(
        queryset=Work.objects.all(),
        help_text=Reference._meta.get_field('work').help_text,
        label=Reference._meta.get_field('work').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:work-autocomplete",
        )
    )
    location = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Reference._meta.get_field('location').help_text,
        label=Reference._meta.get_field('location').verbose_name
    )

    class Meta:
        model = Reference
        fields = [
            'id',
            'legacy_id',
            'work',
            'location',
            
        ]


class WorkListFilter(django_filters.FilterSet):
    legacy_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Work._meta.get_field('legacy_id').help_text,
        label=Work._meta.get_field('legacy_id').verbose_name
    )
    order_code = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Work._meta.get_field('order_code').help_text,
        label=Work._meta.get_field('order_code').verbose_name
    )
    author_name = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Work._meta.get_field('author_name').help_text,
        label=Work._meta.get_field('author_name').verbose_name
    )
    full_quote = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Work._meta.get_field('full_quote').help_text,
        label=Work._meta.get_field('full_quote').verbose_name
    )

    class Meta:
        model = Work
        fields = [
            'id',
            'legacy_id',
            'order_code',
            'author_name',
            'full_quote',
            
        ]

