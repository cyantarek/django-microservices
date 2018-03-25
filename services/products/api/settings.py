import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '********* SET HERE YOUR SECRET *********'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
	'rest_framework',

	'api'
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

WSGI_APPLICATION = 'api.wsgi.application'

DATABASES = {
	'default': {
		'ENGINE': 'djongo',
		'NAME': 'products',
		'HOST': 'mongod',
		'PORT': 27017
	}
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
	'UNAUTHENTICATED_USER': None
}
