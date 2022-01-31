# generated by appcreator

from django.db import models
from django.urls import reverse
from django.contrib.gis.db.models import MultiPolygonField, PointField

from browsing.browsing_utils import model_to_dict
from vocabs.models import SkosConcept


def set_extra(self, **kwargs):
    self.extra = kwargs
    return self


models.Field.set_extra = set_extra


class Event(models.Model):
    ### Ereignis ###
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
    )
    order_code = models.IntegerField(
        blank=True, null=True,
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
        verbose_name="nicht danaach",
        help_text="whatever",
    ).set_extra(
        is_public=True,
    )
    main_text = models.TextField(
        blank=True, null=True,
        verbose_name="Haupttext",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Text1",
    )
    notes_lit = models.TextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Literatur",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Literatur",
    )
    notes_img = models.TextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Abbildungen",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Abbildung",
    )
    notes_facs = models.TextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Faksimiles",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Faksimile",
    )
    notes_archive = models.TextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Archiv",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Archiv",
    )
    notes_text = models.TextField(
        blank=True, null=True,
        verbose_name="Anmerkungen Text",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Anmerkung",
    )
    key_word = models.ManyToManyField(
        SkosConcept,
        related_name='rvn_event_key_word_skosconcept',
        blank=True,
        verbose_name="Stichwort",
        help_text="whatever",
    ).set_extra(
        is_public=True,
    )
    note = models.TextField(
        blank=True, null=True,
        verbose_name="Allgemeine Anmkerungen",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Notizen",
    )
    reference = models.ManyToManyField(
        "Reference",
        related_name='rvn_event_reference_reference',
        blank=True,
        verbose_name="Literatur",
        help_text="whatever",
    ).set_extra(
        is_public=True,
    )
    orig_data_csv = models.TextField(
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
        verbose_name = "Ereignis"

    def __str__(self):
        if self.order_code:
            return "{}".format(self.order_code)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:event_browse')

    @classmethod
    def get_source_table(self):
        return "tblObject_4"

    @classmethod
    def get_natural_primary_key(self):
        return "order_code"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:event_create')

    def get_absolute_url(self):
        return reverse('archiv:event_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:event_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:event_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:event_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:event_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class Reference(models.Model):
    ### Referenz ###
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
    )
    work = models.ForeignKey(
        "Work",
        related_name='rvn_reference_work_work',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Werk",
        help_text="whatever",
    ).set_extra(
        is_public=True,
    )
    location = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Seitenzahl",
        help_text="whatever",
    ).set_extra(
        is_public=True,
    )
    orig_data_csv = models.TextField(
        blank=True,
        null=True,
        verbose_name="The original data"
    ).set_extra(
        is_public=True
    )

    class Meta:

        ordering = [
            'id',
        ]
        verbose_name = "Referenz"

    def __str__(self):
        if self.id:
            return "{}".format(self.id)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:reference_browse')

    @classmethod
    def get_source_table(self):
        return None

    @classmethod
    def get_natural_primary_key(self):
        return "id"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:reference_create')

    def get_absolute_url(self):
        return reverse('archiv:reference_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:reference_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:reference_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:reference_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:reference_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class Work(models.Model):
    ### Literatur ###
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
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
    full_quote = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Langzitat",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="text_Titel",
    )
    orig_data_csv = models.TextField(
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
        if self.order_code:
            return "{}".format(self.order_code)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:work_browse')

    @classmethod
    def get_source_table(self):
        return "tblObject_4"

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
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:work_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:work_detail',
                kwargs={'pk': prev.first().id}
            )
        return False

