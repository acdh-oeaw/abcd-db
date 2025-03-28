# Anton Bruckner Chronologie Datenbank
[![Test](https://github.com/acdh-oeaw/abcd-db/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/abcd-db/actions/workflows/test.yml)
[![flake8 Lint](https://github.com/acdh-oeaw/abcd-db/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/abcd-db/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/acdh-oeaw/abcd-db/branch/master/graph/badge.svg?token=0068S12XV0)](https://codecov.io/gh/acdh-oeaw/abcd-db)
[![Build and push to DockerHub](https://github.com/acdh-oeaw/abcd-db/actions/workflows/build.yml/badge.svg)](https://github.com/acdh-oeaw/abcd-db/actions/workflows/build.yml)


short description of the project

## install

* clone the repo
* change into the project's root directory e.g. `cd abcd-db`
* create a virtual environment e.g. `virutalenv env` and activate it `source env/bin/activate`
* install required packages `pip install -r requirements_dev.txt`
* [to connect to a postgres-db called `abcd_db` with user/password `postgres` run `source source set_env_variables.sh`] (this will set environment variables declared in `env.default)
* run migrations `python manage.py migrate`
* start the dev sever `python manage.py runserver`
* go to [http://127.0.0.1:8000](http://127.0.0.1:8000/) and check if everything works

## data ingest

* run `python manage.py import_abcd_data`

(this script processes data from the gsheets [Bruckner_DB_20220204](https://docs.google.com/spreadsheets/d/1oG_DsN_MkAXg8mR-WmPANMyuZYbWllsNLQ6blGE_70E) and [Literatur_DB_20220204](https://docs.google.com/spreadsheets/d/17lfhVUW6RYSdwkSoginK0uKMI_Dn-iGPgAw1wcKgnHI))

### NER

* install spacy
* install needed spacy model `python -m spacy download de_core_news_lg`
* run `python manage.py import_ners`

## Docker

At the ACDH-CH we use a centralized database-server. So instead of spawning a database for each service our services are talking to a database on this centralized db-server. This setup is reflected in the dockerized setting as well, meaning it expects an already existing database (either on your host, e.g. accessible via 'localhost' or some remote one)

### building the image

* `docker build -t abcd:latest .`
* `docker build -t abcd:latest --no-cache .`


### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

* `docker run -it --network="host" --rm --env-file env.default --name abcd abcd:latest`

-----

This project was bootstraped by [djangobase-cookiecutter](https://github.com/acdh-oeaw/djangobase-cookiecutter)