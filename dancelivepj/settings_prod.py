from .settings import *


DEBUG = False

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),
        'NAME': env('NAME'), 
        'USER': env('USER') ,
        'PASSWORD': env('PASSWORD'), 
        'HOST': env('HOST'),
        'PORT': env('PORT'), 
    }
}