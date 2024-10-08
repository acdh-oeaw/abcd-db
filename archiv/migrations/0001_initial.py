# Generated by Django 3.2.12 on 2022-02-03 18:39

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vocabs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Work",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "order_code",
                    models.CharField(
                        blank=True,
                        help_text="Lit.0001",
                        max_length=250,
                        null=True,
                        verbose_name="Ordnungsnummer",
                    ),
                ),
                (
                    "author_name",
                    models.CharField(
                        blank=True,
                        help_text="whatever",
                        max_length=250,
                        null=True,
                        verbose_name="Autorenname",
                    ),
                ),
                (
                    "full_quote",
                    models.CharField(
                        blank=True,
                        help_text="whatever",
                        max_length=250,
                        null=True,
                        verbose_name="Langzitat",
                    ),
                ),
                (
                    "orig_data_csv",
                    ckeditor.fields.RichTextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
            ],
            options={
                "verbose_name": "Literatur",
                "ordering": ["order_code"],
            },
        ),
        migrations.CreateModel(
            name="Reference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        help_text="whatever",
                        max_length=250,
                        null=True,
                        verbose_name="Seitenzahl",
                    ),
                ),
                (
                    "orig_data_csv",
                    ckeditor.fields.RichTextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
                (
                    "work",
                    models.ForeignKey(
                        blank=True,
                        help_text="whatever",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_reference_work_work",
                        to="archiv.work",
                        verbose_name="Werk",
                    ),
                ),
            ],
            options={
                "verbose_name": "Referenz",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "id",
                    models.IntegerField(
                        help_text="YYYYMMDD+curnr",
                        primary_key=True,
                        serialize=False,
                        verbose_name="Ordnungsnummer",
                    ),
                ),
                (
                    "date_written",
                    models.CharField(
                        blank=True,
                        help_text="helptext for date_written",
                        max_length=250,
                        null=True,
                        verbose_name="Datum",
                    ),
                ),
                (
                    "not_before",
                    models.DateField(
                        blank=True,
                        help_text="whatever",
                        null=True,
                        verbose_name="nicht bevor",
                    ),
                ),
                (
                    "not_after",
                    models.DateField(
                        blank=True,
                        help_text="whatever",
                        null=True,
                        verbose_name="nicht danach",
                    ),
                ),
                (
                    "main_text",
                    ckeditor.fields.RichTextField(
                        blank=True,
                        help_text="whatever",
                        null=True,
                        verbose_name="Haupttext",
                    ),
                ),
                (
                    "notes_lit",
                    ckeditor.fields.RichTextField(
                        blank=True,
                        help_text="whatever",
                        null=True,
                        verbose_name="Anmerkungen Literatur",
                    ),
                ),
                (
                    "notes_img",
                    ckeditor.fields.RichTextField(
                        blank=True,
                        help_text="whatever",
                        null=True,
                        verbose_name="Anmerkungen Abbildungen",
                    ),
                ),
                (
                    "notes_facs",
                    ckeditor.fields.RichTextField(
                        blank=True,
                        help_text="whatever",
                        null=True,
                        verbose_name="Anmerkungen Faksimiles",
                    ),
                ),
                (
                    "notes_archive",
                    ckeditor.fields.RichTextField(
                        blank=True,
                        help_text="whatever",
                        null=True,
                        verbose_name="Anmerkungen Archiv",
                    ),
                ),
                (
                    "notes_text",
                    ckeditor.fields.RichTextField(
                        blank=True,
                        help_text="whatever",
                        null=True,
                        verbose_name="Anmerkungen Text",
                    ),
                ),
                (
                    "note",
                    ckeditor.fields.RichTextField(
                        blank=True,
                        help_text="whatever",
                        null=True,
                        verbose_name="Allgemeine Anmkerungen",
                    ),
                ),
                (
                    "orig_data_csv",
                    ckeditor.fields.RichTextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
                (
                    "key_word",
                    models.ManyToManyField(
                        blank=True,
                        help_text="whatever",
                        related_name="rvn_event_key_word_skosconcept",
                        to="vocabs.SkosConcept",
                        verbose_name="Stichwort",
                    ),
                ),
                (
                    "reference",
                    models.ManyToManyField(
                        blank=True,
                        help_text="whatever",
                        related_name="rvn_event_reference_reference",
                        to="archiv.Reference",
                        verbose_name="Literatur",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ereignis",
                "ordering": ["id"],
            },
        ),
    ]
