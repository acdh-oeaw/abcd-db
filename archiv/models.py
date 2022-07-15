import ciso8601
import time
from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
from ckeditor.fields import RichTextField
from typesense import api_call
from next_prev import next_in_order, prev_in_order

from acdh_cfts_pyutils import TYPESENSE_CLIENT as ts_client, CFTS_SCHEMA_NAME
from browsing.browsing_utils import model_to_dict
from gnd.models import GndPersonBase


TS_SCHEMA_NAME = 'abcd-db'


TS_SCHEMA = {
    'name': TS_SCHEMA_NAME,
    'fields': [
        {
            'name': 'id',
            'type': 'string',
        },
        {
            'name': 'rec_id',
            'type': 'string'
        },
        {
            'name': 'resolver',
            'type': 'string'
        },
        {
            'name': 'project',
            'type': 'string',
            'facet': True
        },
        {
            'name': 'title',
            'type': 'string'
        },
        {
            'name': 'full_text',
            'type': 'string'
        },
        {
            'name': 'date',
            'type': 'int64',
            'facet': True,
        },
        {
            'name': 'year',
            'type': 'int32',
            'optional': True,
            'facet': True
        },
        {
            'name': 'persons',
            'type': 'string[]',
            'facet': True,
            'optional': True
        },
        {
            'name': 'places',
            'type': 'string[]',
            'facet': True,
            'optional': True
        },
        {
            'name': 'wabs',
            'type': 'string[]',
            'facet': True,
            'optional': True
        },
        {
            'name': 'works',
            'type': 'string[]',
            'facet': True,
            'optional': True
        },
        {
            'name': 'keywords',
            'type': 'string[]',
            'facet': True,
            'optional': True
        }
    ],
    'default_sorting_field': 'date',
}


def set_extra(self, **kwargs):
    self.extra = kwargs
    return self


models.Field.set_extra = set_extra


class AbcdBase(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Erstellt am",
        help_text="Zeit der Erstellung des Objektes (ab 2022-05-25)"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Letzte Änderung",
        help_text="Zeit der letzten Änderung"
    )

    class Meta:
        abstract = True


class Wab(AbcdBase):
    title = models.CharField(
        max_length=250, blank=True, null=True
    )
    wab_id = models.CharField(
        max_length=3, unique=True,
        verbose_name="WAB Nummer",
        help_text="z.B. 003, 021, 123"
    )
    date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Maschinenlesbare Datierung",
        help_text="z.B. 1874-12-24"
    )
    date_written = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Datierung des Werkes",
        help_text="z.B. Nicht vor September 1772"
    )
    wab_xml = models.TextField(
        blank=True,
        null=True,
        verbose_name="XML/MEI des Werkes"
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen",
        help_text="Anmerkungen und Erläuterungen"
    )
    status = models.TextField(
        blank=True,
        null=True,
        verbose_name="Berabeitungsstand",
        help_text="Internes Feld zur Dokumentation der Verknüpfungen von WAB zu Ereignis"
    )

    class Meta:

        ordering = [
            'wab_id',
        ]

    def __str__(self):
        return f"{self.title}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:wab_browse')

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:wab_create')

    def get_absolute_url(self):
        return reverse('archiv:wab_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:wab_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:wab_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse(
                'archiv:wab_detail',
                kwargs={'pk': next.id}
            )
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse(
                'archiv:wab_detail',
                kwargs={'pk': prev.id}
            )
        return False


class Place(AbcdBase):
    title = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Ortsname',
        help_text='z.B. Ansfelden'
    )
    geonames_id = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="GeoNames ID",
        help_text="z.B. 'https://www.geonames.org/2782480/ansfelden.html'"
    )
    long = models.FloatField(
        blank=True, null=True,
        verbose_name="Breitengrad",
        help_text="Breitengrad, z.B. '14.29004'",
    )
    lat = models.FloatField(
        blank=True, null=True,
        verbose_name="Längengrad",
        help_text="Längengrad, z.B. '48.20969'",
    )
    remarks = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen generell",
        help_text="Anmerkungen zum Ort"
    ).set_extra(
        is_public=True,
        data_lookup="text_Text1",
    )
    notes_lit = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Literatur",
        help_text="Literatur zum Ort",
    ).set_extra(
        is_public=True,
        data_lookup="text_Literatur",
    )
    work = models.ManyToManyField(
        'Work',
        blank=True,
        related_name="work_referenced_in_place",
        verbose_name="Literatur",
        help_text="Literaturangaben zu diesem Ort"
    )
    notes_img = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Abbildungen",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Abbildung",
    )
    notes_facs = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Faksimiles",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Faksimile",
    )
    notes_archive = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Archiv",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Archiv",
    )
    status = models.TextField(
        blank=True,
        null=True,
        verbose_name="Berabeitungsstand",
        help_text="Internes Feld zur Dokumentation der Verknüpfungen von Ort zu Ereignis"
    )

    def __str__(self):
        return f"{self.title}"

    def field_dict(self):
        return model_to_dict(self)

    class Meta:

        ordering = [
            'title',
        ]

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:place_browse')

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:place_create')

    def get_absolute_url(self):
        return reverse('archiv:place_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:place_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:place_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse(
                'archiv:place_detail',
                kwargs={'pk': next.id}
            )
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse(
                'archiv:place_detail',
                kwargs={'pk': prev.id}
            )
        return False


class Institution(AbcdBase):
    title = models.CharField(max_length=250, blank=True, null=True)

    class Meta:

        ordering = [
            'title',
        ]

    def __str__(self):
        return f"{self.title}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:institution_browse')

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:institution_create')

    def get_absolute_url(self):
        return reverse('archiv:institution_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:institution_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:institution_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse(
                'archiv:institution_detail',
                kwargs={'pk': next.id}
            )
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse(
                'archiv:institution_detail',
                kwargs={'pk': prev.id}
            )
        return False


class Person(GndPersonBase):
    title = models.CharField(max_length=250, blank=True, null=True)
    bruckner_entity = models.BooleanField(
        default=False,
        verbose_name="Link zu Bruckner XML"
    )
    bruckner_entity_id = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name="Bruckner-Entity-ID",
    )
    bruckner_entity_xml = models.TextField(
        blank=True,
        null=True,
        verbose_name="MEI:XML"
    )
    oeml_uri = models.URLField(
        blank=True,
        null=True,
        verbose_name="Link zu ÖML Eintrag"
    )
    ablo_uri = models.URLField(
        blank=True,
        null=True,
        verbose_name="Link zu ABLO Eintrag"
    )
    remarks = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen generell",
        help_text="Anmerkungen zur Person"
    ).set_extra(
        is_public=True,
        data_lookup="text_Text1",
    )
    notes_lit = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Literatur",
        help_text="Literatur zur Person",
    ).set_extra(
        is_public=True,
        data_lookup="text_Literatur",
    )
    work = models.ManyToManyField(
        'Work',
        blank=True,
        related_name="work_referenced_in_person",
        verbose_name="Literatur",
        help_text="Literaturangaben zu dieser Person"
    )
    notes_img = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Abbildungen",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Abbildung",
    )
    notes_facs = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Faksimiles",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Faksimile",
    )
    notes_archive = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Archiv",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Archiv",
    )
    status = models.TextField(
        blank=True,
        null=True,
        verbose_name="Berabeitungsstand",
        help_text="Internes Feld zur Dokumentation der Verknüpfungen von Person zu Ereignis"
    )

    class Meta:

        ordering = [
            'id',
        ]

    def __str__(self):
        return f"{self.title}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:person_browse')

    @classmethod
    def get_natural_primary_key(self):
        return "id"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:person_create')

    def get_absolute_url(self):
        return reverse('archiv:person_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:person_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:person_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse(
                'archiv:person_detail',
                kwargs={'pk': next.id}
            )
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse(
                'archiv:person_detail',
                kwargs={'pk': prev.id}
            )
        return False


class Event(AbcdBase):
    """ Ereignis """
    legacy_id = models.CharField(
        max_length=300, blank=True,
        db_index=True,
        verbose_name="Legacy ID"
    ).set_extra(
        is_public=True,
        data_lookup="OF_ID",
    )
    id = models.IntegerField(
        primary_key=True,
        db_index=True,
        verbose_name="Ordnungsnummer",
        help_text="YYYYMMDD+curnr",
    ).set_extra(
        is_public=True,
        data_lookup="input_Sortiercode",
    )
    date_written = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Datum",
        help_text="helptext for date_written",
    ).set_extra(
        is_public=True,
        data_lookup="input_Datum",
    )
    not_before = models.DateField(
        blank=True, null=True,
        verbose_name="nicht bevor",
        help_text="whatever",
    ).set_extra(
        is_public=True,
    )
    not_after = models.DateField(
        blank=True, null=True,
        verbose_name="nicht danach",
        help_text="whatever",
    ).set_extra(
        is_public=True,
    )
    main_text = RichTextField(
        blank=True, null=True,
        verbose_name="Haupttext",
        help_text="Beschreibung des Ereignis",
    ).set_extra(
        is_public=True,
        data_lookup="text_Text1",
    )
    notes_lit = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Literatur",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Literatur",
    )
    notes_img = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Abbildungen",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Abbildung",
    )
    notes_facs = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Faksimiles",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Faksimile",
    )
    notes_archive = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Archiv",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Archiv",
    )
    notes_text = RichTextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Text",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Anmerkung",
    )
    key_word = models.TextField(
        blank=True,
        null=True,
        verbose_name="Stichwort",
        help_text="Feld für interne Notizen und Stichworte",
    ).set_extra(
        is_public=True,
    )
    note = RichTextField(
        blank=True, null=True,
        verbose_name="Allgemeine Anmerkungen",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Notizen",
    )
    wab = models.ManyToManyField(
        'Wab',
        blank=True,
        related_name="rvn_wab_mentioned_in",
        verbose_name="erwähnte Bruckner Werke (WAB)"
    )
    person = models.ManyToManyField(
        'Person',
        blank=True,
        related_name="rvn_person_mentioned_in",
        verbose_name="erwähnte Personen"
    )
    place = models.ManyToManyField(
        'Place',
        blank=True,
        related_name="place_mentioned_in",
        verbose_name="erwähnte Orte"
    )
    institution = models.ManyToManyField(
        'Institution',
        blank=True,
        related_name="institution_mentioned_in",
        verbose_name="erwähnte Institutionen"
    )
    work = models.ManyToManyField(
        'Work',
        blank=True,
        related_name="work_referenced_in",
        verbose_name="Literatur",
        help_text="Literaturangaben zu diesem Event"
    )
    full_text = models.TextField(
        blank=True,
        null=True,
        verbose_name="Volltext Feld",
        help_text="Volltext Feld (technisch notwendig)"
    )

    class Meta:

        ordering = [
            'id',
        ]
        verbose_name = "Ereignis"

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
        if not self.not_before:
            try:
                dto = datetime.strptime(str(self.id)[:8], '%Y%m%d').date()
            except ValueError:
                dto = None
            self.not_before = dto
        if self.main_text:
            self.full_text = self.join_search_fields()
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        if self.id:
            return "{}".format(self.id)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def search_field_names(self):
        text_fields = [
            'main_text',
            'notes_lit',
            'notes_img',
            'notes_facs',
            'notes_archive',
            'notes_text',
            'date_written',
            'note',
            'key_word'
        ]
        return text_fields

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:event_browse')

    @classmethod
    def get_source_table(self):
        return "tblObject_4"

    @classmethod
    def get_natural_primary_key(self):
        return "id"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:event_create')

    @classmethod
    def ts_recreate_schema(self):
        try:
            ts_client.collections[TS_SCHEMA_NAME].delete()
        except api_call.ObjectNotFound:
            pass
        ts_collection = ts_client.collections.create(TS_SCHEMA)
        return ts_collection

    @classmethod
    def ts_update_index(self, records):
        ts_client.collections[TS_SCHEMA_NAME].documents.import_(
            records,
            {'action': 'upsert'}
        )
        print("Done indexing abcd-db")
        ts_client.collections[CFTS_SCHEMA_NAME].documents.import_(
            records,
            {'action': 'upsert'}
        )
        print("Done indexing cfts")
        return "indexed"

    def ts_make_document(self):
        doc = {
            'project': TS_SCHEMA_NAME,
            'id': f"{TS_SCHEMA_NAME}__{str(self.id)}",
            'rec_id': str(self.id),
            'resolver': f"https://abcd.acdh-dev.oeaw.ac.at{self.get_absolute_url()}",
            'full_text': self.full_text,
            'year': int(str(self.id)[:4]),
            'wabs': [f"{x}" for x in self.wab.all()],
            'works': [f"{x}" for x in self.work.all()],
            'persons': [f"{x}" for x in self.person.all()],
            'places': [f"{x}" for x in self.place.all()]
        }
        if self.date_written is not None:
            doc['title'] = f"{self.date_written}"
        else:
            doc['title'] = f"Eintrag ID {self.id}"
        try:
            doc['date'] = int(time.mktime(self.not_before.timetuple()))
        except AttributeError:
            date_str = f"{str(self.id)[:4]}-01-01"
            ts = ciso8601.parse_datetime(date_str)
            doc['date'] = int(time.mktime(ts.timetuple()))
        return doc

    def join_search_fields(self):
        full_text = set([getattr(self, x, '') for x in self.search_field_names() if getattr(self, x, None) is not None])
        full_text_str = " ".join([x for x in full_text if isinstance(x, str) and x != 'nan'])
        return " ".join(f"{strip_tags(full_text_str)} {self.id}".split())

    def get_absolute_url(self):
        return reverse('archiv:event_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:event_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:event_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse(
                'archiv:event_detail',
                kwargs={'pk': next.id}
            )
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse(
                'archiv:event_detail',
                kwargs={'pk': prev.id}
            )
        return False


class Work(AbcdBase):
    """ Literatur """
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
    ).set_extra(
        is_public=True,
        data_lookup="OF_ID",
    )
    order_code = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Ordnungsnummer",
        help_text="Lit.0001",
    ).set_extra(
        is_public=True,
        data_lookup="input_Nummer",
    )
    author_name = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Autorenname",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="input_Autor",
    )
    year = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Erscheinungsjahr",
        help_text="Erscheingungsjahr"
    )
    short_quote = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Kurzzitat",
        help_text="Kurzzitat: Autor, Titel, Ornungsnummer (leere Felder werden automatisiert befüllt)"
    )
    full_quote = RichTextField(
        blank=True,
        null=True,
        verbose_name="Langzitat",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Titel",
    )
    orig_data_csv = RichTextField(
        blank=True,
        null=True,
        verbose_name="The original data"
    ).set_extra(
        is_public=True
    )

    class Meta:

        ordering = [
            'order_code',
        ]
        verbose_name = "Literatur"

    def __str__(self):
        if self.short_quote is None:
            return f"{self.author_name}, {self.work_title()}, {self.order_code}"
        else:
            return f"{self.short_quote}"

    def save(self, *args, **kwargs):
        super(Work, self).save(*args, **kwargs)
        if not self.short_quote:
            self.short_quote = strip_tags(self.__str__())
        super(Work, self).save(*args, **kwargs)

    def field_dict(self):
        return model_to_dict(self)

    def work_title(self):
        if self.full_quote:
            title_parts = self.full_quote.split(':')
            if len(title_parts) > 1:
                return title_parts[1].split(',')[0]

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:work_browse')

    @classmethod
    def get_source_table(self):
        return "tblObject_2"

    @classmethod
    def get_natural_primary_key(self):
        return "order_code"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:work_create')

    def get_absolute_url(self):
        return reverse('archiv:work_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:work_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:work_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse(
                'archiv:work_detail',
                kwargs={'pk': next.id}
            )
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse(
                'archiv:work_detail',
                kwargs={'pk': prev.id}
            )
        return False
