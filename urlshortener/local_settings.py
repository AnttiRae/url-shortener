# local settings.
# use this file to assign settings for the current environment.
# This one is used for github actions
# In production set debug to false and use proper secret key

SECRET_KEY = 'django-insecure-y9xb2c#sp#*5i-tyzz%jrjy5iriy#bdh#n&$+=hhb8*kgde8m^'
DEBUG = True


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '0.0.0.0',
        'PORT': '4444',
    }
}
