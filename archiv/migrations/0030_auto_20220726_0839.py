# Generated by Django 3.2.13 on 2022-07-26 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("archiv", "0029_auto_20220627_0820"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                help_text="Zeit der Erstellung des Objektes (ab 2022-05-25)",
                verbose_name="Erstellt am",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="person",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Zeit der letzten Änderung",
                verbose_name="Letzte Änderung",
            ),
        ),
    ]
