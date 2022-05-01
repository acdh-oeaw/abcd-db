# Generated by Django 3.2.12 on 2022-05-01 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0015_auto_20220501_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='wab',
            name='note',
            field=models.TextField(blank=True, help_text='Anmerkungen und Erläuterungen', null=True, verbose_name='Anmerkungen'),
        ),
        migrations.AlterField(
            model_name='work',
            name='short_quote',
            field=models.CharField(blank=True, help_text='Kurzzitat: Autor, Titel, Ornungsnummer (leere Felder werden automatisiert befüllt)', max_length=500, null=True, verbose_name='Kurzzitat'),
        ),
    ]