#!/usr/bin/env bash
# create_fixtures.sh

# make sure you ran `pip install django-fixture-magic` and added `'fixture_magic'` to INSTALLED_APPS
source env/bin/activate

echo "create fixtures_event"
python manage.py dump_object archiv.event 174210000 192704035 192704045 > fixtures_event.json

echo "create fixtures_wab"
python manage.py dump_object archiv.wab 40 41 > fixtures_wab.json

echo "create fixtures_work"
python manage.py dump_object archiv.work 999 > fixtures_work.json

echo "merging fixturs"
python manage.py merge_fixtures fixtures_event.json fixtures_wab.json fixtures_work.json > archiv/fixtures/dump.json

echo "delete fixtures"
rm fixtures_work.json
rm fixtures_wab.json
rm fixtures_event.json

echo "done"