# Generated by Django 3.2.15 on 2022-11-28 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("archiv", "0035_auto_20221128_0936"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
              CREATE TRIGGER vector_column_trigger
              BEFORE INSERT OR UPDATE OF full_text, vector_column
              ON archiv_event
              FOR EACH ROW EXECUTE PROCEDURE
              tsvector_update_trigger(
                vector_column, 'pg_catalog.german', full_text
              );

              UPDATE archiv_event SET vector_column = NULL;
            """,
            reverse_sql="""
              DROP TRIGGER IF EXISTS vector_column_trigger
              ON archiv_event;
            """,
        ),
    ]