import django_tables2 as tables

from browsing.browsing_utils import MergeColumn

from .models import SkosCollection, SkosConcept, SkosTechnicalCollection


class SkosCollectionTable(tables.Table):

    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = SkosCollection
        sequence = ("id", "pref_label")
        attrs = {"class": "table table-responsive table-hover"}


class SkosTechnicalCollectionTable(tables.Table):

    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = SkosTechnicalCollection
        sequence = ("id", "pref_label")
        attrs = {"class": "table table-responsive table-hover"}


class SkosConceptTable(tables.Table):

    id = tables.LinkColumn(verbose_name="ID")
    remarks = tables.columns.TemplateColumn(
        template_code="{{ record.remarks|safe }}",
        verbose_name="Anmerkungen generell"
    )

    class Meta:
        model = SkosConcept
        sequence = ("id", "pref_label", "collection")
        attrs = {"class": "table table-responsive table-hover"}
