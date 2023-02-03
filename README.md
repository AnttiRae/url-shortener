# URL Shortener


## Running (development):
- make a python virtual environment with `python -m venv env` and activate env. with `source env/bin/activate`
- install dependencies: `pip install -r requirements.txt`
- make sure local_settings.py is configured and placed in project folder (urlshortener)
- after setting up the database (postgres in this case) run migrations: `python manage.py migrate`
- run the project with `python manage.py runserver`. 

Note: In production a WSGI server like gunicorn or uwsgi would be used to run the project behind a proxy server such as Nginx  

## Dependencies:
- Django
- Django restframework
- Postgres


## Example local_settings.py
```
# local settings.
# use this file to assign settings for the current environment.
# In production set debug to false and use proper secret key

SECRET_KEY = 'django-insecure-y9xb2c#sp#*5i-tyzz%jrjy5iriy#bdh#n&$+=hhb8*kgde8m^'
DEBUG = True


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'urlshortener',
        'USER': 'postgres',
        'PASSWORD': 'toor',
        'HOST': '0.0.0.0',
        'PORT': '4444',
    }
}
```
