# Generated by Django 3.2.12 on 2022-03-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archiv", "0010_auto_20220318_1736"),
    ]

    operations = [
        migrations.CreateModel(
            name="Wab",
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
                ("title", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "wab_id",
                    models.CharField(
                        help_text="z.B. 003, 021, 123",
                        max_length=3,
                        unique=True,
                        verbose_name="WAB Nummer",
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        blank=True,
                        help_text="z.B. 1874-12-24",
                        null=True,
                        verbose_name="Maschinenlesbare Datierung",
                    ),
                ),
                (
                    "date_written",
                    models.CharField(
                        blank=True,
                        help_text="z.B. Nicht vor September 1772",
                        max_length=250,
                        null=True,
                        verbose_name="Datierung des Werkes",
                    ),
                ),
                (
                    "wab_xml",
                    models.TextField(
                        blank=True, null=True, verbose_name="XML/MEI des Werkes"
                    ),
                ),
            ],
            options={
                "ordering": ["wab_id"],
            },
        ),
    ]
