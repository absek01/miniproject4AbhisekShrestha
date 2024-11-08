# settings.py

import os
from pathlib import Path

# Define BASE_DIR to point to the root of the project
BASE_DIR = Path(__file__).resolve().parent.parent


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # This is optional if you're using custom templates
        'APP_DIRS': True,  # This allows loading templates from your apps
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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required for admin
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for admin
    'django.contrib.messages.middleware.MessageMiddleware',  # Required for admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # For SQLite database
        'NAME': BASE_DIR / 'db.sqlite3',  # Path to the SQLite database file
    }
}


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'  # Redirects users after login
LOGOUT_REDIRECT_URL = '/'  # Redirects users after logout

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'myproject.urls'

SECRET_KEY = 'z3R7F5zA3bML9uixL0aKYUecy8QW4RLDJh2gtsZt73FhD75XaG'