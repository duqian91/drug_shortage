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

    Uploads Excel file, clean and commit data into database
- [ ] drug_shortage_api

    Run databse DIN with Canadian Drugs Shortage Databse API and commit result into databse
- [ ] display_table

    Display data

## About
This django project is used to fetch Canadian Drug Shortage api from Gespharx8 exported spreadsheet. 

The django boilerplate comes from https://github.com/archatas/django-myproject