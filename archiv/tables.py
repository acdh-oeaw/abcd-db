# generated by appcreator
import django_tables2 as tables

from browsing.browsing_utils import MergeColumn
from .models import Event, Work, Place, Person, Institution, Wab


class ResultsTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    main_text = tables.columns.TemplateColumn(
        template_code="{{ record.main_text|safe }}"
    )

    class Meta:
        model = Event
        fields = (
            "id",
            "date_written",
            "main_text",
        )
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class InstitutionTable(tables.Table):

    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Institution
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class PersonTable(tables.Table):

    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Person
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class PlaceTable(tables.Table):

    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Place
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class EventTable(tables.Table):

    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")
    person = tables.columns.ManyToManyColumn()
    place = tables.columns.ManyToManyColumn()
    institution = tables.columns.ManyToManyColumn()
    key_word = tables.columns.ManyToManyColumn()
    work = tables.columns.ManyToManyColumn()
    wab = tables.columns.ManyToManyColumn()
    main_text = tables.columns.TemplateColumn(
        template_code="{{ record.main_text|safe }}"
    )

    class Meta:
        model = Event
        sequence = (
            "id",
            "date_written",
            "main_text",
        )
        attrs = {"class": "table table-responsive table-hover"}


class WorkTable(tables.Table):

    id = tables.LinkColumn(verbose_name="ID")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Work
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class WabTable(tables.Table):

    id = tables.LinkColumn(verbose_name="ID")

    class Meta:
        model = Wab
        sequence = (
            "id",
            "wab_id",
        )
        attrs = {"class": "table table-responsive table-hover"}
