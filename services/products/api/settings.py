import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '********* SET HERE YOUR SECRET *********'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
	'django.contrib.staticfiles',
	'rest_framework',
	'rest_framework_swagger',

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

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")
