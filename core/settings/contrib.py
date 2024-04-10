# coding=utf-8
"""
core.settings.contrib
"""
from core.settings.utils import ensure_unique_app_labels
from .base import *  # noqa
# Override base settings from geonode
from .legacy_geonode_settings import *
from core.settings.celery_settings import *  # noqa
import os
try:
    from .secret import IUCN_API_KEY  # noqa
except ImportError:
    IUCN_API_KEY = ''


STOP_WORDS = (
    'a', 'an', 'and', 'if', 'is', 'the', 'in', 'i', 'you', 'other',
    'this', 'that', 'to',
)

STATICFILES_STORAGE = 'bims.storage.NoSourceMapsStorage'
STATICFILES_FINDERS += (
    'pipeline.finders.PipelineFinder',
)

# Django-allauth related settings
AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Django grappelli need to be added before django.contrib.admin
INSTALLED_APPS = (
    'grappelli',
    'colorfield',
    'polymorphic',
    'webpack_loader',
    'ckeditor_uploader',
    'django_admin_inline_paginator',
    'django_celery_results'
) + INSTALLED_APPS

# Grapelli settings
GRAPPELLI_ADMIN_TITLE = 'Bims Admin Page'

INSTALLED_APPS += (
    # AppConfig Hook to fix issue from geonode
    'core.config_hook',
    'bims.signals',
    'allauth',
    'allauth.account',
    'rolepermissions',
    'rest_framework',
    'rest_framework_gis',
    'celery',
    'pipeline',
    'modelsdoc',
    'contactus',
    # 'django_prometheus',
    'crispy_forms',
    'sass',
    'rangefilter',
    'preferences',
    'sorl.thumbnail',
    'ckeditor',
    'django_json_widget',
    'django_forms_bootstrap'
)

INSTALLED_APPS += (
    'taggit',
)
INSTALLED_APPS = (
    'rest_framework.authtoken',
) + INSTALLED_APPS

if os.environ.get('SENTRY_KEY'):
    import sentry_sdk
    sentry_sdk.init(
        dsn=os.environ.get('SENTRY_KEY'),
        traces_sample_rate=1.0,
    )

# workaround to get flatpages picked up in installed apps.
INSTALLED_APPS += (
    'django.contrib.flatpages',
    'django.contrib.sites',
)

# Set templates
try:
    TEMPLATES[0]['DIRS'] = [
        absolute_path('core', 'base_templates'),
        absolute_path('bims', 'templates'),
        absolute_path('sass', 'templates'),
        absolute_path('td_biblio', 'templates'),
        absolute_path('pesticide', 'templates'),
    ] + TEMPLATES[0]['DIRS']

    TEMPLATES[0]['OPTIONS']['context_processors'] += [
        'bims.context_processor.add_recaptcha_key',
        'bims.context_processor.custom_navbar_url',
        'bims.context_processor.google_analytic_key',
        'bims.context_processor.bing_api_key',
        'bims.context_processor.bims_preferences',
        'bims.context_processor.application_name',
        'bims.context_processor.site_ready',
        'bims.context_processor.download_request_message',
        'bims.context_processor.download_request_purpose',
        'bims_theme.context_processor.bims_custom_theme',
        'preferences.context_processors.preferences_cp',
    ]
except KeyError:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                # project level templates
                absolute_path('core', 'base_templates'),
                absolute_path('bims', 'templates'),
                absolute_path('sass', 'templates'),
                absolute_path('td_biblio', 'templates'),
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',

                    # `allauth` needs this from django
                    'django.template.context_processors.request',
                    'bims.context_processor.add_recaptcha_key',
                    'bims.context_processor.custom_navbar_url',
                    'bims.context_processor.google_analytic_key',
                    'bims.context_processor.application_name',
                    'bims.context_processor.download_request_message',
                    'bims_theme.context_processor.bims_custom_theme',
                ],
            },
        },
    ]

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/home/web/static'

# Additional locations of static files
STATICFILES_DIRS = [
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    absolute_path('core', 'base_static'),
    absolute_path('bims', 'static'),
    absolute_path('sass', 'static'),
    absolute_path('scripts', 'static'),
    absolute_path('td_biblio', 'static'),
    absolute_path('pesticide', 'static'),
]

MIDDLEWARE += (
    'bims.middleware.VisitorTrackingMiddleware',
)

TESTING = sys.argv[1:2] == ['test']
if not TESTING and not on_travis:
    INSTALLED_APPS += (
        'easyaudit',
    )
    MIDDLEWARE += (
        'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
    )
# for middleware in MIDDLEWARE_CLASSES:
#     if middleware not in MIDDLEWARE:
#         MIDDLEWARE += (middleware,)

# Defines whether to log model related events,
# such as when an object is created, updated, or deleted
DJANGO_EASY_AUDIT_WATCH_MODEL_EVENTS = True

# Defines whether to log user authentication events,
# such as logins, logouts and failed logins.
DJANGO_EASY_AUDIT_WATCH_AUTH_EVENTS = True

# Defines whether to log URL requests made to the project
DJANGO_EASY_AUDIT_WATCH_REQUEST_EVENTS = False

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
LOGIN_REDIRECT_URL = "/"

AUTH_WITH_EMAIL_ONLY = ast.literal_eval(os.environ.get(
        'AUTH_WITH_EMAIL_ONLY', 'True'))

if AUTH_WITH_EMAIL_ONLY:
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_FORMS = {
        'signup': 'bims.forms.CustomSignupForm',
    }
    ACCOUNT_AUTHENTICATION_METHOD = 'email'
else:
    INSTALLED_APPS += (
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',
        'allauth.socialaccount.providers.github',
    )


INSTALLED_APPS = ensure_unique_app_labels(INSTALLED_APPS)
# ROLEPERMISSIONS_MODULE = 'roles.settings.roles'

# Remove pinax notifications from installed apps
if 'pinax.notifications' in INSTALLED_APPS:
    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS.remove('pinax.notifications')
    INSTALLED_APPS = tuple(INSTALLED_APPS)

IUCN_API_URL = 'http://apiv3.iucnredlist.org/api/v3'

# django modelsdoc settings
MODELSDOC_APPS = ('bims', 'td_biblio',)

MODELSDOC_OUTPUT_FORMAT = 'rst'
MODELSDOC_MODEL_WRAPPER = 'modelsdoc.wrappers.ModelWrapper'
MODELSDOC_FIELD_WRAPPER = 'modelsdoc.wrappers.FieldWrapper'
MODELSDOC_INCLUDE_AUTO_CREATED = True

# contact us email
SERVER_EMAIL = os.environ.get('ADMIN_EMAILS', 'admin@kartoza.com')
CONTACT_US_EMAIL = os.environ.get('CONTACT_US_EMAIL', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', CONTACT_US_EMAIL)

# site tracking stats settings
TRACK_PAGEVIEWS = True
TRACK_AJAX_REQUESTS = False
TRACK_REFERER = True
TRACK_IGNORE_STATUS_CODES = [301, 303, 403, 404, 405, 410]

DJANGO_EASY_AUDIT_UNREGISTERED_CLASSES_EXTRA = [
    # 'layers.Layer',
    'people.Profile',
    'bims.Pageview',
    'bims.Visitor',
    'bims.Taxonomy',
    'bims.LocationContext',
    'bims.LocationContextGroup',
    'bims.SearchProcess',
    'flatpages.FlatPage',
    'td_biblio.author'
]

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d '
                      '%(thread)d %(message)s'
        },
        'simple': {
            'format': '%(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'celery': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'celery.log',
            'formatter': 'simple',
            'maxBytes': 1024 * 1024 * 10,  # 10 mb
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"], "level": "ERROR", },
        "bims": {
            "handlers": ["console"], "level": "DEBUG", },
        "geonode": {
            "handlers": ["console"], "level": "INFO", },
        "geonode.qgis_server": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "gsconfig.catalog": {
            "handlers": ["console"], "level": "ERROR", },
        "owslib": {
            "handlers": ["console"], "level": "ERROR", },
        "pycsw": {
            "handlers": ["console"], "level": "ERROR", },
        "celery": {
            'handlers': ['celery', 'console'], 'level': 'DEBUG', },
    },
}

ASYNC_SIGNALS_GEONODE = ast.literal_eval(os.environ.get(
        'ASYNC_SIGNALS_GEONODE', 'False'))

# Set institutionID default value
INSTITUTION_ID_DEFAULT = os.environ.get('INSTITUTION_ID_DEFAULT', 'bims')

ACCOUNT_APPROVAL_REQUIRED = True
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_ADAPTER = 'bims.adapters.account_adapter.AccountAdapter'
ACCOUNT_EMAIL_VERIFICATION = 'none'
CELERY_TASK_PROTOCOL = 1

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}

SELENIUM_DRIVER = os.environ.get(
    'SELENIUM_DRIVER',
    'http://hub:4444/wd/hub')

# Enable or disable SASS
try:
    SASS_ENABLED = ast.literal_eval(os.environ.get('SASS_ENABLED', 'False'))
except ValueError:
    SASS_ENABLED = False

# Bims site preferences
BIMS_PREFERENCES = {
    'enable_module_filter': ast.literal_eval(
        os.environ.get('ENABLE_MODULE_FILTER', 'True')
    ),
    'enable_catchment_filter': ast.literal_eval(
        os.environ.get('ENABLE_CATCHMENT_FILTER', 'False')
    ),
    'enable_ecoregion_filter': ast.literal_eval(
        os.environ.get('ENABLE_ECOREGION_FILTER', 'False')
    ),
    'enable_user_boundary_filter': ast.literal_eval(
        os.environ.get('ENABLE_USER_BOUNDARY_FILTER', 'False')
    ),
    'enable_download_data_from_map': ast.literal_eval(
        os.environ.get('ENABLE_DOWNLOAD_DATA_FROM_MAP', 'False')
    ),
    'geoserver_location_site_layer': os.environ.get(
        'GEOSERVER_LOCATION_SITE_LAYER',
        ''
    ),
    'empty_location_site_cluster': os.environ.get(
        'EMPTY_LOCATION_SITE_CLUSTER',
        'empty_location_site_cluster'
    ),
    'recaptcha_key': os.environ.get(
        'RECAPTCHA_KEY',
        ''
    ),
    'enable_upload_data': ast.literal_eval(
        os.environ.get('ENABLE_UPLOAD_DATA', 'True')
    )
}

# Remove geonode session middleware
if (
    'geonode.security.middleware.SessionControlMiddleware' in
        MIDDLEWARE
):
    MIDDLEWARE_CLASSES_LIST = list(MIDDLEWARE)
    MIDDLEWARE_CLASSES_LIST.remove(
        'geonode.security.middleware.SessionControlMiddleware'
    )
    MIDDLEWARE = tuple(MIDDLEWARE_CLASSES_LIST)


# CKEDITOR configurations
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'contentsCss': [
            '/static/js/libs/bootstrap-4.0.0/css/bootstrap.min.css',
            '/static/css/base.css'
        ],
        'removePlugins': 'stylesheetparser',
        'allowedContent': True,
        'extraAllowedContent': 'span(*) btn(*)'
    },
}

# SORL THUMBNAIL SETTINGS
THUMBNAIL_COLORSPACE = None
THUMBNAIL_PRESERVE_FORMAT = True

# add bims url
ROOT_URLCONF = 'core.urls'


CELERY_TASK_QUEUES += (
    Queue('search',
          GEONODE_EXCHANGE, routing_key='search', priority=0),
    Queue('geocontext',
          GEONODE_EXCHANGE, routing_key='geocontext', priority=0),
)
CELERY_TASK_TRACK_STARTED = True
CELERY_TRACK_STARTED = True
TASK_TRACK_STARTED = True
CELERY_IGNORE_RESULT = False
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': 'cache:11211',
    }
}

FILE_UPLOAD_PERMISSIONS = 0o644
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'

# CKEDITOR CONFIGURATIONS
CKEDITOR_UPLOAD_PATH = 'ckeditor/'


ACCOUNT_LOGOUT_REDIRECT_URL = '/'
CELERY_RESULT_BACKEND = 'django-db'
