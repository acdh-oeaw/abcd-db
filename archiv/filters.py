# generated by appcreator
import django_filters
from django import forms

from dal import autocomplete
from archiv.filter_utils import SchrederFilter
from . models import (
    Event,
    Work,
    Person,
    Place,
    Institution,
    Wab
)

NUMBER_LOOKUP_CHOICES = [
    ('exact', 'Gleich'),
    ('gt', 'Größer als'),
    ('lt', 'Kleiner als')
]

CHAR_LOOKUP_CHOICES = [
    ('icontains', 'Enthält'),
    ('iexact', 'Gleich'),
    ('istartswith', 'Beginnt mit'),
    ('iendswith', 'Endet mit')
]


class EventSimpleFilter(SchrederFilter):
    full_text = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Event._meta.get_field('full_text').help_text,
        label=Event._meta.get_field('full_text').verbose_name
    )
    main_text = django_filters.CharFilter(
        method='scheder_filtering'
    )

    class Meta:
        model = Event
        fields = [
            'full_text',
            'main_text'
        ]


class EventListFilter(SchrederFilter):
    legacy_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('legacy_id').help_text,
        label=Event._meta.get_field('legacy_id').verbose_name,
    )
    date_written = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('date_written').help_text,
        label=Event._meta.get_field('date_written').verbose_name,
    )
    main_text = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text="Beispiel: 'Richard Wagner' findet alle Datensätze,\
            die 'Richard Wagner' im Haupttext enthalten, aber auch z.B.\
                'Richard Wagners Opern",
        label="Einfache Suche im Haupttext",
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    main_text_scheder = django_filters.CharFilter(
        method='scheder_filtering',
        field_name='main_text',
        help_text="Beispiel: +Richard +Wagner -Verein = alle Datensätze,\
            die Richard UND Wagner aber NICHT Verein enthalten, werden angezeigt",
        label="Erweiterte Suche im Haupttext"
    )
    notes_lit = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Event._meta.get_field('notes_lit').help_text,
        label=Event._meta.get_field('notes_lit').verbose_name
    )
    notes_img = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Event._meta.get_field('notes_img').help_text,
        label=Event._meta.get_field('notes_img').verbose_name
    )
    notes_facs = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Event._meta.get_field('notes_facs').help_text,
        label=Event._meta.get_field('notes_facs').verbose_name
    )
    notes_archive = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Event._meta.get_field('notes_archive').help_text,
        label=Event._meta.get_field('notes_archive').verbose_name
    )
    notes_text = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Event._meta.get_field('notes_text').help_text,
        label=Event._meta.get_field('notes_text').verbose_name
    )
    key_word = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Event._meta.get_field('key_word').help_text,
        label=Event._meta.get_field('key_word').verbose_name
    )
    work = django_filters.ModelMultipleChoiceFilter(
        queryset=Work.objects.all(),
        help_text=Event._meta.get_field('work').help_text,
        label=Event._meta.get_field('work').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/archiv-ac/work-autocomplete",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    person = django_filters.ModelMultipleChoiceFilter(
        queryset=Person.objects.all(),
        help_text=Event._meta.get_field('person').help_text,
        label=Event._meta.get_field('person').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/archiv-ac/person-autocomplete",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    place = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Event._meta.get_field('place').help_text,
        label=Event._meta.get_field('place').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/archiv-ac/place-autocomplete",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    institution = django_filters.ModelMultipleChoiceFilter(
        queryset=Institution.objects.all(),
        help_text=Event._meta.get_field('institution').help_text,
        label=Event._meta.get_field('institution').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/archiv-ac/institution-autocomplete",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
            },
        )
    )
    wab = django_filters.ModelMultipleChoiceFilter(
        queryset=Wab.objects.all(),
        help_text=Event._meta.get_field('wab').help_text,
        label=Event._meta.get_field('wab').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/archiv-ac/wab-autocomplete",
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

    class Meta:
        model = Event
        fields = [
            'id',
            'legacy_id',
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
        label=Work._meta.get_field('order_code').verbose_name,
        widget=forms.TextInput(attrs={'autofocus': True})
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


class PlaceListFilter(django_filters.FilterSet):

    title = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Place._meta.get_field('title').help_text,
        label=Place._meta.get_field('title').verbose_name,
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    class Meta:
        model = Place
        fields = '__all__'


class PersonListFilter(django_filters.FilterSet):

    title = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Person._meta.get_field('title').help_text,
        label='Name',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    gnd_gnd_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Person._meta.get_field('gnd_gnd_id').help_text,
        label='GND-id (Gemeinsame Normdatei, DNB)'
    )
    ablo_uri = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Person._meta.get_field('ablo_uri').help_text,
        label=Person._meta.get_field('ablo_uri').verbose_name
    )
    oeml_uri = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Person._meta.get_field('oeml_uri').help_text,
        label=Person._meta.get_field('oeml_uri').verbose_name
    )

    class Meta:
        model = Person
        exclude = [
            'gnd_payload'
        ]


class InstitutionListFilter(django_filters.FilterSet):

    title = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Institution._meta.get_field('title').help_text,
        label=Institution._meta.get_field('title').verbose_name
    )

    class Meta:
        model = Institution
        fields = '__all__'


class WabListFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Wab._meta.get_field('title').help_text,
        label="Titel",
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    class Meta:
        model = Wab
        fields = '__all__'
