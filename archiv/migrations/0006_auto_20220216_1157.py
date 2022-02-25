# Generated by Django 3.2.12 on 2022-02-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0005_auto_20220205_0740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='event',
            name='work',
            field=models.ManyToManyField(blank=True, related_name='work_referenced_in', to='archiv.Work'),
        ),
        migrations.AlterField(
            model_name='event',
            name='person',
            field=models.ManyToManyField(blank=True, related_name='rvn_person_mentioned_in', to='archiv.Person'),
        ),
    ]