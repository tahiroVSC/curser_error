"""
Django settings for Triatlon project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from pathlib import Path
import os
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')


SECRET_KEY = "sldjflskdjflsdjslflk"
DEBUG = True


ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    
    'jazzmin',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'ckeditor',
    
    # apps
    'apps.Abonements',
    'apps.About',
    'apps.application',
    'apps.contacts',
    'apps.Faq','apps.files',
    'apps.Offering',
    'apps.Review',
    'apps.Services',
    'apps.trainer',
    'apps.TrainZone.apps.TrainzoneConfig',
    'apps.vacancy',
    'apps.schedule',
    'apps.homepage',
]



REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Triatlon.urls'

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

WSGI_APPLICATION = 'Triatlon.wsgi.application'


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGES = (
    ('ru', _('Russian')),
    ('ky', _('Kyrgyz')),
)
LANGUAGE_CODE = 'ru'


TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "Triathlon Center",  # Заголовок админ-панели
    "site_header": "Triathlon Center",  # Заголовок на экране входа
    "site_brand": "Triathlon Center",  # Бренд в верхней части админ-панели
    "welcome_sign": "Добро пожаловать в Triathlon Center",  # Приветственное сообщение
    "site_title": "Triathlon Center",  # Заголовок админ-панели
    "site_header": "Triathlon Center",  # Заголовок на экране входа
    "site_brand": "Triathlon Center",  # Бренд в верхней части админ-панели
    "welcome_sign": "Добро пожаловать в Triathlon Center",  # Приветственное сообщение
    "search_model": [],  # Модели, доступные для поиска
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "apps.Abonement.models.Abonement": "horizontal_tabs"},
    "topmenu_links": [
        {"name": "Home", "url": "admin:index",
            "permissions": ["auth.view_user"]},
    ],
    "show_sidebar": True,
    "show_language_chooser": True,  # Включить выбор языка в админ-панели
    "custom_css": None,  # Путь к пользовательскому CSS-файлу (если нужен)
    "show_ui_builder": True,  # Показать UI Builder
    "menu": [
        {
            "app": "index",  # Имя вашего приложения Django
            "name": "Основные параметры",  # Имя модели
            "icon": "fa fa-cogs",  # Иконка для меню
            "models": [
                {
                    "name": "Первая модель",  # Имя вашей модели
                    "icon": "fa fa-cog",  # Иконка для модели
                    "model": "index.Settings",  # Имя модели в формате "app_label.model_name"
                },
                # Добавьте другие модели, если необходимо
            ],
        },
        # Добавьте другие приложения и модели, если необходимо
    ],

}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-success",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-success",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "superhero",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

# EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_PORT = int(os.getenv('EMAIL_PORT'))  # Преобразуем в целое число
# EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS').lower() in ['true', '1', 'yes']  # Преобразуем в булево значение
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'  # URL to jQuery
CKEDITOR_IMAGE_BACKEND = "pillow"  # Путь к пакету Pillow для обработки изображений
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',  # Вы можете настроить свою собственную панель инструментов CKEditor
        'height': 300,
        'width': 800,
    },
}
