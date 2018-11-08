import os

BASE_DIR                                            = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG                                               = False ## runserver da True olmalı
ALLOWED_HOSTS                                       = ["*"]

STATIC_URL                                          = '/static/'
STATIC_ROOT                                         = os.path.join(BASE_DIR, 'static')              ##### Sunucu için
# STATIC_ROOT                                         = ''                                          ### Lokal için
# STATICFILES_DIRS                                    = (os.path.join(BASE_DIR, 'static'),)         ### Lokal için


INSTALLED_APPS                                      = [
                                                        'django.contrib.admin',
                                                        'django.contrib.auth',
                                                        'django.contrib.contenttypes',
                                                        'django.contrib.sessions',
                                                        'django.contrib.messages',
                                                        'django.contrib.staticfiles',
                                                        'uygulama.apps.UygulamaConfig',
                                                    ]

DATABASES                                           = {
                                                           'default': {
                                                               'ENGINE': 'django.db.backends.postgresql_psycopg2',
                                                               'NAME': 'blogdb',
                                                               'USER': 'bloguser',
                                                               'PASSWORD': 'Test+123',
                                                               'HOST': '127.0.0.1',
                                                               'PORT': '5432',
                                                                'CONN_MAX_AGE': 600,
                                                           },
                                                       }

MIDDLEWARE                                          = [
                                                            'django.middleware.security.SecurityMiddleware',
                                                            'django.contrib.sessions.middleware.SessionMiddleware',
                                                            'django.middleware.common.CommonMiddleware',
                                                            'django.middleware.csrf.CsrfViewMiddleware',
                                                            'django.contrib.auth.middleware.AuthenticationMiddleware',
                                                            'django.contrib.messages.middleware.MessageMiddleware',
                                                            'django.middleware.clickjacking.XFrameOptionsMiddleware',

                                                        ]

TEMPLATES                                           = [
                                                        {
                                                            'BACKEND': 'django.template.backends.django.DjangoTemplates',
                                                            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

ROOT_URLCONF                                        = 'django_blog.urls'
LANGUAGE_CODE                                       = 'tr_TR'
TIME_ZONE                                           = 'Europe/Istanbul'
USE_I18N                                            = True
USE_L10N                                            = True
USE_TZ                                              = True


DATA_UPLOAD_MAX_NUMBER_FIELDS                       = 99999 # Toplu silme işleminde limit
SECRET_KEY                                          = 's-&qy=k7&yze*_$jz2lbb%2=k9+kv+3w0n%xe-&h_+55%-)%w345345345e'
WSGI_APPLICATION                                    = 'django_blog.wsgi.application'

if DEBUG:
                                                        INTERNAL_IPS = ('78.187.60.13', '127.0.0.1')
                                                        MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
                                                        INSTALLED_APPS += ('debug_toolbar',)
                                                        DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
                                                        DEBUG_TOOLBAR_PANELS = [
                                                            'debug_toolbar.panels.sql.SQLPanel',
                                                            'debug_toolbar.panels.staticfiles.StaticFilesPanel',
                                                        ]
