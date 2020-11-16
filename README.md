# Django drug_shortage

## Steps to get started with local dev
* Create a virtualenv
```python
python3 -m venv myprojectvenv
```

* Modify manage.py to use the right setting file
```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE',  'myproject.settings.dev')
```

* Install postgresql from official site, download latest version. Default port 5432
    * Log into postgresql shell 
```
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```
* Create secrets.json in settings directory
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

* Run python migration
* Ready to go with http://127.0.0.1:8000/

## Project apps
- [ ] clean_gespharx8_excel

    Use import export django for importing file format

    What is left: complete model and complete view to clean the data upon upload so there are no errors, change file format to excel

- [ ] drug_shortage_api

    Run databse DIN with Canadian Drugs Shortage Databse API and commit result into databse with save()

    Make this task a background task using Celery

    Link retrieved info with foreign key model to link with the model from the first app

- [ ] display_table

    Display data with Queryset. Consider creating a custom manager to better query data

    Don't need to be an app per se. Just display everything

## About
This django project is used to fetch Canadian Drug Shortage api from Gespharx8 exported spreadsheet. 

The django boilerplate comes from https://github.com/archatas/django-myproject