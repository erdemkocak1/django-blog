import os

BASE_DIR                                            = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG                                               = True ## runserver da True olmalı
ALLOWED_HOSTS                                       = ["*"]

STATIC_URL                                          = '/static/'
STATIC_ROOT                                         = os.path.join(BASE_DIR, 'static')              ##### Sunucu için
SESSION_EXPIRE_AT_BROWSER_CLOSE                     = True
SESSION_COOKIE_HTTPONLY                             = False
SESSION_COOKIE_SECURE                               = True
SESSION_SAVE_EVERY_REQUEST                          = True
SESSION_COOKIE_DOMAIN                               = 'blog.coolrio.pw'
SECURE_SSL_REDIRECT                                 = True
# SECURE_SSL_REDIRECT                                 = False                                       ### Lokal için
# STATIC_ROOT                                         = ''                                          ### Lokal için
# STATICFILES_DIRS                                    = (os.path.join(BASE_DIR, 'static'),)         ### Lokal için


INSTALLED_APPS                                      = [
                                                        'django.contrib.admin',
                                                        'django.contrib.auth',
                                                        'django.contrib.contenttypes',
                                                        'django.contrib.sessions',
                                                        'django.contrib.messages',
                                                        'django.contrib.staticfiles',
                                                        'django.contrib.sites',
                                                        'uygulama.apps.UygulamaConfig',
                                                    ]

DATABASES                                           = {
                                                           'default': {
                                                               'ENGINE': 'django.db.backends.postgresql_psycopg2',
                                                               'NAME': 'blogcoolriodb',
                                                               'USER': 'blogkullanici',
                                                               'PASSWORD': 'blogpassword',
                                                               'HOST': '185.122.200.225',
                                                               'PORT': '',
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
