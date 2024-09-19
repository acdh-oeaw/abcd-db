# Generated by Django 3.2.12 on 2022-05-04 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archiv", "0016_auto_20220501_0841"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="key_word",
        ),
        migrations.AddField(
            model_name="event",
            name="key_word",
            field=models.TextField(
                blank=True,
                help_text="Feld für interne Notizen und Stihworte",
                null=True,
                verbose_name="Stichwort",
            ),
        ),
    ]
