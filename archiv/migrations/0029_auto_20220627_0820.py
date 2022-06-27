# Generated by Django 3.2.13 on 2022-06-27 08:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0028_place_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='notes_archive',
            field=ckeditor.fields.RichTextField(blank=True, help_text='whatever', null=True, verbose_name='Anmerkungen Archiv'),
        ),
        migrations.AddField(
            model_name='person',
            name='notes_facs',
            field=ckeditor.fields.RichTextField(blank=True, help_text='whatever', null=True, verbose_name='Anmerkungen Faksimiles'),
        ),
        migrations.AddField(
            model_name='person',
            name='notes_img',
            field=ckeditor.fields.RichTextField(blank=True, help_text='whatever', null=True, verbose_name='Anmerkungen Abbildungen'),
        ),
        migrations.AddField(
            model_name='place',
            name='notes_archive',
            field=ckeditor.fields.RichTextField(blank=True, help_text='whatever', null=True, verbose_name='Anmerkungen Archiv'),
        ),
        migrations.AddField(
            model_name='place',
            name='notes_facs',
            field=ckeditor.fields.RichTextField(blank=True, help_text='whatever', null=True, verbose_name='Anmerkungen Faksimiles'),
        ),
        migrations.AddField(
            model_name='place',
            name='notes_img',
            field=ckeditor.fields.RichTextField(blank=True, help_text='whatever', null=True, verbose_name='Anmerkungen Abbildungen'),
        ),
    ]
