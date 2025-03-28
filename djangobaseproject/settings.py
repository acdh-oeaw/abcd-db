import os
from pathlib import Path

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent
SHARED_URL = "https://shared.acdh.oeaw.ac.at/"
PROJECT_NAME = "abcd"


ACDH_IMPRINT_URL = "https://imprint.acdh.oeaw.ac.at/"
REDMINE_ID = os.environ.get("REDMINE_ID", 19928)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "TZRHHwGV")

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get("DEBUG"):
    DEBUG = True
else:
    DEBUG = False
ADD_ALLOWED_HOST = os.environ.get("ALLOWED_HOST", "*")

ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    ADD_ALLOWED_HOST,
]

GITLAB_TOKEN = os.environ.get("GITLAB_TOKEN")
BRUCKNER_PERSON_URL = "https://gitlab.com/api/v4/projects/34600039/repository/files/100_register%2F101_persons%2FRegister_Personen.xml/raw?ref=main"  # noqa: 501


# Application definition

INSTALLED_APPS = [
    "dal",
    "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "rest_framework",
    "crispy_forms",
    "crispy_bootstrap4",
    "django_filters",
    "django_tables2",
    "ckeditor",
    "django_spaghetti",
    "webpage",
    "browsing",
    "infos",
    "vocabs",
    "archiv",
    "gnd",
    "fixture_magic",
]

SPAGHETTI_SAUCE = {
    "apps": ["archiv", "vocabs"],
    "show_fields": False,
    "exclude": {"auth": ["user"]},
}

CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

ROOT_URLCONF = "djangobaseproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "webpage.webpage_content_processors.installed_apps",
                "webpage.webpage_content_processors.is_dev_version",
                "webpage.webpage_content_processors.get_db_name",
                "webpage.webpage_content_processors.shared_url",
                "webpage.webpage_content_processors.my_app_name",
            ],
        },
    },
]

WSGI_APPLICATION = "djangobaseproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if os.environ.get("POSTGRES_DB"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER", "postgres"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
            "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
            "PORT": os.environ.get("POSTEGRES_PORT", "5432"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "de"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LEGACY_DB_SHEET_ID = "1TLagwMUVUPjFm_JXmMwS3vy0I3dHs9nMxT6xs9yFHv8"
LEGACY_DB_LIT_SHEET_ID = "17lfhVUW6RYSdwkSoginK0uKMI_Dn-iGPgAw1wcKgnHI"
WAB_SEARCH = "1zEL1gn-lcvJL7FUWesNXph6N6Gczk45GVcK9HI1qhdc"
SPECIAL_CHARS_SHEET_ID = "1RGlec8TtxvX-PxfbCvfwg1kQHh76Oai0VyTYQR_8TTE"


styles = [
    {"name": "Gesperrt", "element": "span", "styles": {"letter-spacing": "3px"}},
    {"name": "Italic Title", "element": "h2", "styles": {"font-style": "italic"}},
    {
        "name": "Subtitle",
        "element": "h3",
        "styles": {"color": "#aaa", "font-style": "italic"},
    },
    {
        "name": "Special Container",
        "element": "div",
        "styles": {
            "padding": "5px 10px",
            "background": "#eee",
            "border": "1px solid #ccc",
        },
    },
    {"name": "Marker", "element": "span", "attributes": {"class": "marker"}},
    {"name": "Big", "element": "big"},
    {"name": "Small", "element": "small"},
    {"name": "Typewriter", "element": "tt"},
    {"name": "Computer Code", "element": "code"},
    {"name": "Keyboard Phrase", "element": "kbd"},
    {"name": "Sample Text", "element": "samp"},
    {"name": "Variable", "element": "var"},
    {"name": "Deleted Text", "element": "del"},
    {"name": "Inserted Text", "element": "ins"},
    {"name": "Cited Work", "element": "cite"},
    {"name": "Inline Quotation", "element": "q"},
]

CKEDITOR_CONFIGS = {
    "default": {
        "entities_latin": False,
        "toolbar": "Custom",
        "stylesSet": styles,
        "toolbar_Custom": [
            "/",
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strike",
                    "Subscript",
                    "Superscript",
                    "-",
                    "RemoveFormat",
                    "Undo",
                    "Redo",
                ],
            },  # noqa: E501
            {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
            {
                "name": "insert",
                "items": [
                    "Image",
                    "Flash",
                    "Table",
                    "HorizontalRule",
                    "Smiley",
                    "SpecialChar",
                    "PageBreak",
                    "Iframe",
                ],
            },
            "/",
            {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            {"name": "tools", "items": ["ShowBlocks", "Source"]},
        ],
    }
}

X_FRAME_OPTIONS = "*"
FILTERS_EMPTY_CHOICE_LABEL = None
