from datetime import datetime
from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from django.urls import reverse
from django.utils.html import strip_tags
from ckeditor.fields import RichTextField
from next_prev import next_in_order, prev_in_order

from browsing.browsing_utils import model_to_dict
from gnd.models import GndPersonBase
from vocabs.models import SkosConcept
from .utils import fix_hrefs


def set_extra(self, **kwargs):
    self.extra = kwargs
    return self


models.Field.set_extra = set_extra


class AbcdBase(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Erstellt am",
        help_text="Zeit der Erstellung des Objektes (ab 2022-05-25)",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Letzte Änderung",
        help_text="Zeit der letzten Änderung",
    )

    class Meta:
        abstract = True


class Wab(AbcdBase):
    """Titel aus dem Bruckner Werkverzeichnis"""

    title = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Werk",
        help_text="Werkstitel und WAB Nummer",
    )
    wab_id = models.CharField(
        max_length=3,
        unique=True,
        verbose_name="WAB Nummer",
        help_text="z.B. 003, 021, 123",
    )
    date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Datierung",
        help_text="z.B. 1874-12-24",
    )
    date_written = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        verbose_name="Datierung des Werkes",
        help_text="z.B. Nicht vor September 1772",
    )
    wab_xml = models.TextField(blank=True, null=True, verbose_name="XML/MEI des Werkes")
    note = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen",
        help_text="Anmerkungen und Erläuterungen",
    )
    status = models.TextField(
        blank=True,
        null=True,
        verbose_name="Berabeitungsstand",
        help_text="Internes Feld zur Dokumentation der Verknüpfungen von WAB zu Ereignis",
    )

    class Meta:
        verbose_name = "Werke Bruckners"
        ordering = [
            "wab_id",
        ]

    def __str__(self):
        return f"{self.title}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:wab_browse")

    @classmethod
    def get_createview_url(self):
        return reverse("archiv:wab_create")

    def get_absolute_url(self):
        return reverse("archiv:wab_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("archiv:wab_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse("archiv:wab_edit", kwargs={"pk": self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse("archiv:wab_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse("archiv:wab_detail", kwargs={"pk": prev.id})
        return False


class Place(AbcdBase):
    "Orte, die in den Ereignissen erwähnt werden"
    title = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Ortsname",
        help_text="z.B. Ansfelden",
    )
    geonames_id = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="GeoNames ID",
        help_text="z.B. 'https://www.geonames.org/2782480/ansfelden.html'",
    )
    long = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Breitengrad",
        help_text="Breitengrad, z.B. '14.29004'",
    )
    lat = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Längengrad",
        help_text="Längengrad, z.B. '48.20969'",
    )
    remarks = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen generell",
        help_text="Anmerkungen zum Ort",
    ).set_extra(
        is_public=True,
        data_lookup="text_Text1",
    )
    notes_lit = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen Literatur",
        help_text="Literatur zum Ort",
    ).set_extra(
        is_public=True,
        data_lookup="text_Literatur",
    )
    work = models.ManyToManyField(
        "Work",
        blank=True,
        related_name="work_referenced_in_place",
        verbose_name="Bibliographie",
        help_text="Literaturangaben zu diesem Ort",
    )
    notes_img = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen Abbildungen",
        help_text="Anmerkungen zum Abschnitt Abbildungen",
    ).set_extra(
        is_public=True,
        data_lookup="text_Abbildung",
    )
    notes_facs = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen Faksimiles",
        help_text="Anmerkungen zum Abschnitt Faksimiles",
    ).set_extra(
        is_public=True,
        data_lookup="text_Faksimile",
    )
    notes_archive = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen Archiv",
        help_text="Anmerkungen zum Abschnitt Archiv",
    ).set_extra(
        is_public=True,
        data_lookup="text_Archiv",
    )
    status = models.TextField(
        blank=True,
        null=True,
        verbose_name="Berabeitungsstand",
        help_text="Internes Feld zur Dokumentation der Verknüpfungen von Ort zu Ereignis",
    )

    def __str__(self):
        return f"{self.title}"

    def field_dict(self):
        return model_to_dict(self)

    class Meta:

        ordering = [
            "title",
        ]

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:place_browse")

    @classmethod
    def get_createview_url(self):
        return reverse("archiv:place_create")

    def get_absolute_url(self):
        return reverse("archiv:place_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("archiv:place_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse("archiv:place_edit", kwargs={"pk": self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse("archiv:place_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse("archiv:place_detail", kwargs={"pk": prev.id})
        return False


class Institution(AbcdBase):
    title = models.CharField(max_length=250, blank=True, null=True)

    class Meta:

        ordering = [
            "title",
        ]

    def __str__(self):
        return f"{self.title}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:institution_browse")

    @classmethod
    def get_createview_url(self):
        return reverse("archiv:institution_create")

    def get_absolute_url(self):
        return reverse("archiv:institution_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("archiv:institution_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse("archiv:institution_edit", kwargs={"pk": self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse("archiv:institution_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse("archiv:institution_detail", kwargs={"pk": prev.id})
        return False


class Person(GndPersonBase):
    "Personen (und Personengruppen), die in den Ereignissen erwähnt werden"
    title = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Voller Name",
        help_text="Vorname Nachname",
    )
    surname = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Nachname"
    )
    bruckner_entity = models.BooleanField(
        default=False, verbose_name="Link zu Bruckner XML"
    )
    bruckner_entity_id = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name="Bruckner-Entity-ID",
    )
    bruckner_entity_xml = models.TextField(
        blank=True, null=True, verbose_name="MEI:XML"
    )
    oeml_uri = models.URLField(
        blank=True, null=True, verbose_name="Link zu ÖML Eintrag"
    )
    ablo_uri = models.URLField(
        blank=True, null=True, verbose_name="Link zu ABLO Eintrag"
    )
    remarks = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen generell",
        help_text="Anmerkungen zur Person",
    ).set_extra(
        is_public=True,
        data_lookup="text_Text1",
    )
    notes_lit = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen Literatur",
        help_text="Literatur zur Person",
    ).set_extra(
        is_public=True,
        data_lookup="text_Literatur",
    )
    work = models.ManyToManyField(
        "Work",
        blank=True,
        related_name="work_referenced_in_person",
        verbose_name="Bibliographie",
        help_text="Literaturangaben zu dieser Person",
    )
    notes_img = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen Abbildungen",
        help_text="Anmerkungen zum Abschnitt Abbildungen",
    ).set_extra(
        is_public=True,
        data_lookup="text_Abbildung",
    )
    notes_facs = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen Faksimiles",
        help_text="Anmerkungen zum Abschnitt Faksimiles",
    ).set_extra(
        is_public=True,
        data_lookup="text_Faksimile",
    )
    notes_archive = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen Archiv",
        help_text="Anmerkungen zum Abschnitt Archiv",
    ).set_extra(
        is_public=True,
        data_lookup="text_Archiv",
    )
    status = models.TextField(
        blank=True,
        null=True,
        verbose_name="Berabeitungsstand",
        help_text="Internes Feld zur Dokumentation der Verknüpfungen von Person zu Ereignis",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Erstellt am",
        help_text="Zeit der Erstellung des Objektes (ab 2022-05-25)",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Letzte Änderung",
        help_text="Zeit der letzten Änderung",
    )

    class Meta:

        ordering = [
            "surname",
        ]

    @classmethod
    def search_field_names(self):
        text_fields = [
            "remarks",
            "notes_lit",
            "notes_img",
            "notes_facs",
            "notes_archive",
        ]
        return text_fields

    def save(self, *args, **kwargs):
        if self.gnd_pref_name is not None:
            name = self.gnd_pref_name.split(", ")
            self.surname = name[0]
        else:
            try:
                name = self.title.split(" ")
            except AttributeError:
                name = False
            if name:
                self.surname = name[len(name) - 1].replace("(", "").replace(")", "")
        fix_hrefs(self)
        super(GndPersonBase, self).save(*args, **kwargs)

    @classmethod
    def submit(self, *args, **kwargs):
        super(GndPersonBase, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:person_browse")

    @classmethod
    def get_natural_primary_key(self):
        return "id"

    @classmethod
    def get_createview_url(self):
        return reverse("archiv:person_create")

    def get_absolute_url(self):
        return reverse("archiv:person_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("archiv:person_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse("archiv:person_edit", kwargs={"pk": self.id})

    def get_next(self):
        try:
            next = next_in_order(self)
        except ValueError:
            next = False
        if next:
            return reverse("archiv:person_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        try:
            prev = prev_in_order(self)
        except ValueError:
            prev = False
        if prev:
            return reverse("archiv:person_detail", kwargs={"pk": prev.id})
        return False

    def check_normdata(self):
        if self.gnd_gnd_id or self.oeml_uri or self.ablo_uri:
            return True
        else:
            return False


class Event(AbcdBase):
    """Ereignisse aus und um das Leben und Werk Anton Bruckners"""

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
        help_text="Datierung des Eintrages",
    ).set_extra(
        is_public=True,
        data_lookup="input_Datum",
    )
    not_before = models.DateField(
        blank=True,
        null=True,
        verbose_name="nicht bevor",
        help_text="Maschinenlesbare Datierung des Eintrages.\
            Bei einem mehrtägigem Ereigniss wird das Anfangsdatum verzeichnet.",
    ).set_extra(
        is_public=True,
    )
    not_after = models.DateField(
        blank=True,
        null=True,
        verbose_name="nicht danach",
        help_text="Maschinenlesbare Datierung des Eintrages.\
            Bei einem mehrtägigem Ereigniss wird das Enddatum verzeichnet.",
    ).set_extra(
        is_public=True,
    )
    main_text = RichTextField(
        blank=True,
        null=True,
        verbose_name="Haupttext",
        help_text="Beschreibung des Ereignis",
    ).set_extra(
        is_public=True,
        data_lookup="text_Text1",
    )
    notes_lit = RichTextField(
        blank=True,
        null=True,
        verbose_name="Literatur",
        help_text="Anmerkungen zum Abschnitt Literatur",
    ).set_extra(
        is_public=True,
        data_lookup="text_Literatur",
    )
    notes_img = RichTextField(
        blank=True,
        null=True,
        verbose_name="Abbildungen",
        help_text="Anmerkungen zum Abschnitt Abbildungen",
    ).set_extra(
        is_public=True,
        data_lookup="text_Abbildung",
    )
    notes_facs = RichTextField(
        blank=True,
        null=True,
        verbose_name="Faksimiles",
        help_text="Anmerkungen zum Abschnitt Faksimiles",
    ).set_extra(
        is_public=True,
        data_lookup="text_Faksimile",
    )
    notes_archive = RichTextField(
        blank=True,
        null=True,
        verbose_name="Archiv",
        help_text="Anmerkungen zum Abschnitt Archiv",
    ).set_extra(
        is_public=True,
        data_lookup="text_Archiv",
    )
    notes_text = RichTextField(
        blank=True,
        null=True,
        verbose_name="Anmerkungen",
        help_text="Anmerkungen zum Abschnitt Anmerkung",
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
        blank=True,
        null=True,
        verbose_name="Allgemeine Anmerkungen",
        help_text="Allgemeine Anmerkungen",
    ).set_extra(
        is_public=True,
        data_lookup="text_Notizen",
    )
    wab = models.ManyToManyField(
        "Wab",
        blank=True,
        related_name="rvn_wab_mentioned_in",
        verbose_name="erwähnte Bruckner Werke (WAB)",
        help_text="Verknüpfungen zu Bruckners Werken",
    )
    person = models.ManyToManyField(
        "Person",
        blank=True,
        related_name="rvn_person_mentioned_in",
        verbose_name="erwähnte Personen",
        help_text="Verknüpfungen zu erwähnten Personen",
    )
    place = models.ManyToManyField(
        "Place",
        blank=True,
        related_name="place_mentioned_in",
        verbose_name="erwähnte Orte",
        help_text="Verknüpfungen zu erwähnten Orten",
    )
    institution = models.ManyToManyField(
        "Institution",
        blank=True,
        related_name="institution_mentioned_in",
        verbose_name="erwähnte Institutionen",
        help_text="Verknüpfungen zu erwähnten Institutionen",
    )
    work = models.ManyToManyField(
        "Work",
        blank=True,
        related_name="work_referenced_in",
        verbose_name="Bibliographie",
        help_text="Literaturangaben zu diesem Ereignis",
    )
    concept = models.ManyToManyField(
        SkosConcept,
        blank=True,
        related_name="concept_for_event",
        verbose_name="Systematisches Schlagwort",
        help_text="Diese Schlagworte werden in einer eigenen Liste geführt",
    )
    full_text = models.TextField(
        blank=True,
        null=True,
        verbose_name="Volltext Feld",
        help_text="Volltext Feld (technisch notwendig)",
    )
    vector_column = SearchVectorField(null=True)

    class Meta:

        ordering = [
            "id",
        ]
        verbose_name = "Ereignis"
        indexes = (GinIndex(fields=["vector_column"]),)

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
        if not self.not_before:
            try:
                dto = datetime.strptime(str(self.id)[:8], "%Y%m%d").date()
            except ValueError:
                dto = None
            self.not_before = dto
        if self.main_text:
            self.full_text = self.join_search_fields()
        fix_hrefs(self)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def search_field_names(self):
        text_fields = [
            "main_text",
            "notes_lit",
            "notes_img",
            "notes_facs",
            "notes_archive",
            "notes_text",
            "date_written",
            "note",
            "key_word",
        ]
        return text_fields

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:event_browse")

    @classmethod
    def get_source_table(self):
        return "tblObject_4"

    @classmethod
    def get_natural_primary_key(self):
        return "id"

    @classmethod
    def get_createview_url(self):
        return reverse("archiv:event_create")

    def join_search_fields(self):
        full_text = set(
            [
                getattr(self, x, "")
                for x in self.search_field_names()
                if getattr(self, x, None) is not None
            ]
        )
        full_text_str = " ".join(
            [x for x in full_text if isinstance(x, str) and x != "nan"]
        )
        return " ".join(f"{strip_tags(full_text_str)} {self.id}".split())

    def get_absolute_url(self):
        return reverse("archiv:event_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("archiv:event_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse("archiv:event_edit", kwargs={"pk": self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse("archiv:event_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse("archiv:event_detail", kwargs={"pk": prev.id})
        return False


class Work(AbcdBase):
    """Referenzierte und zitierte Sekundärliteratur"""

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
        help_text="Name der Autorin/des Autors",
    ).set_extra(
        is_public=True,
        data_lookup="input_Autor",
    )
    year = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Erscheinungsjahr",
        help_text="Erscheingungsjahr",
    )
    short_quote = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Kurzzitat",
        help_text="Kurzzitat: Autor, Titel, Ornungsnummer (leere Felder werden automatisiert befüllt)",
    )
    full_quote = RichTextField(
        blank=True,
        null=True,
        verbose_name="Langzitat",
        help_text="Vollsständige bibliographische Angabe",
    ).set_extra(
        is_public=True,
        data_lookup="text_Titel",
    )

    class Meta:

        ordering = [
            "order_code",
        ]
        verbose_name = "Literatur"

    def search_field_names(self):
        text_fields = [
            "full_quote",
        ]
        return text_fields

    def __str__(self):
        if self.short_quote is None:
            return f"{self.author_name}, {self.work_title()}, {self.order_code}"
        else:
            return f"{self.short_quote}"

    def save(self, *args, **kwargs):
        super(Work, self).save(*args, **kwargs)
        if not self.short_quote:
            self.short_quote = strip_tags(self.__str__())
        fix_hrefs(self)
        super(Work, self).save(*args, **kwargs)

    def field_dict(self):
        return model_to_dict(self)

    def work_title(self):
        if self.full_quote:
            title_parts = self.full_quote.split(":")
            if len(title_parts) > 1:
                return title_parts[1].split(",")[0]

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:work_browse")

    @classmethod
    def get_source_table(self):
        return "tblObject_2"

    @classmethod
    def get_natural_primary_key(self):
        return "order_code"

    @classmethod
    def get_createview_url(self):
        return reverse("archiv:work_create")

    def get_absolute_url(self):
        return reverse("archiv:work_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("archiv:work_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse("archiv:work_edit", kwargs={"pk": self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return reverse("archiv:work_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return reverse("archiv:work_detail", kwargs={"pk": prev.id})
        return False
