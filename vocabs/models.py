from django.db import models
from django.conf import settings
from django.urls import reverse
from next_prev import next_in_order, prev_in_order
from browsing.browsing_utils import model_to_dict

from mptt.models import MPTTModel, TreeForeignKey


DEFAULT_LANG = getattr(settings, 'VOCABS_DEFAULT_LANG', 'deu')


class SkosTechnicalCollection(models.Model):
    """
    Class to link SkosConcepts to properties where they are used in.
    Needed for e.g. autocompletes, showing only Concepts matching the current property
    """
    pref_label = models.CharField(
        blank=True,
        null=True,
        max_length=300,
        verbose_name="Model and property name",
        help_text="e.g. 'Artifact__artefact_type",
    )

    def __str__(self):
        return f"{self.pref_label}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('vocabs:skostechnicalcollection_browse')

    @classmethod
    def get_createview_url(self):
        return reverse('vocabs:skostechnicalcollection_create')

    def get_absolute_url(self):
        return reverse('vocabs:skostechnicalcollection_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('vocabs:skostechnicalcollection_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('vocabs:skostechnicalcollection_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return next.get_absolute_url()
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return prev.get_absolute_url()
        return False


class SkosCollection(models.Model):
    """
    SKOS collections are labeled and/or ordered groups of SKOS concepts.
    Collections are useful where a group of concepts shares something in common,
    and it is convenient to group them under a common label, or
    where some concepts can be placed in a meaningful order.
    Miles, Alistair, and Sean Bechhofer. "SKOS simple knowledge
    organization system reference. W3C recommendation (2009)."
    """

    pref_label = models.CharField(
        blank=True,
        null=True,
        max_length=300,
        verbose_name="skos:prefLabel",
        help_text="Collection label or name",
    )
    definition = models.TextField(
        blank=True,
        null=True,
        verbose_name="elaborate definition of the collection",
        help_text="definition"
    )
    source_uri = models.CharField(
        null=True,
        blank=True,
        max_length=300,
        verbose_name="source URI",
        help_text="URI of the Resource"
    )

    def __str__(self):
        if self.source_uri is not None:
            return f"{self.pref_label} <{self.source_uri}>"
        else:
            return f"{self.pref_label}"

    @classmethod
    def get_natural_primary_key(self):
        return "pref_label"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('vocabs:skoscollection_browse')

    @classmethod
    def get_createview_url(self):
        return reverse('vocabs:skoscollection_create')

    def get_absolute_url(self):
        return reverse('vocabs:skoscollection_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('vocabs:skoscollection_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('vocabs:skoscollection_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return next.get_absolute_url()
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return prev.get_absolute_url()
        return False


class SkosConcept(MPTTModel):
    """
    A SKOS concept can be viewed as an idea or notion; a unit of thought.
    However, what constitutes a unit of thought is subjective,
    and this definition is meant to be suggestive, rather than restrictive.
    Miles, Alistair, and Sean Bechhofer. "SKOS simple knowledge
    organization system reference. W3C recommendation (2009)."
    """
    pref_label = models.CharField(
        max_length=300,
        verbose_name="Label",
        help_text="Preferred label for concept"
    )
    definition = models.TextField(
        blank=True,
        null=True,
        verbose_name="elaborate definition of the concept",
        help_text="skos:definition"
    )
    collection = models.ForeignKey(
        'SkosCollection',
        null=True,
        blank=True,
        verbose_name="Teil der Skos-Kollektion",
        help_text="Collection that this concept is a member of",
        related_name="has_members",
        on_delete=models.SET_NULL,
    )
    broader_concept = TreeForeignKey(
        'self',
        verbose_name="skos:broader",
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name="narrower_concepts",
        help_text="Concept with a broader meaning that this concept inherits from"
    )
    source_uri = models.CharField(
        null=True,
        blank=True,
        max_length=300,
        verbose_name="source URI",
        help_text="URI of the Resource"
    )
    tech_collection = models.ManyToManyField(
        'SkosTechnicalCollection',
        blank=True,
        verbose_name="member of skos:Collection",
        help_text="Collection that this concept is a member of",
        related_name="has_members",
    )

    class MPTTMeta:
        parent_attr = 'broader_concept'

    def __str__(self):
        return f"{self.pref_label}"

    @classmethod
    def get_natural_primary_key(self):
        return "pref_label"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('vocabs:skosconcept_browse')

    @classmethod
    def get_createview_url(self):
        return reverse('vocabs:skosconcept_create')

    def get_absolute_url(self):
        return reverse('vocabs:skosconcept_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('vocabs:skosconcept_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('vocabs:skosconcept_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = next_in_order(self)
        if next:
            return next.get_absolute_url()
        return False

    def get_prev(self):
        prev = prev_in_order(self)
        if prev:
            return prev.get_absolute_url()
        return False
