"""OWASP Nest test configuration."""


from settings.base import Base


class Test(Base):
    """Test configuration."""

    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "test-cache",
        },
    }

    IS_TEST_ENVIRONMENT = True

    CSRF_COOKIE_SECURE = False
    SECURE_HSTS_SECONDS = 0
    SECURE_PROXY_SSL_HEADER = None  # type: ignore[assignment]  # Django accepts None to disable.
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False

    # use sqlite in-memory for tests to avoid PostgreSQL dependencies
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    }

    # remove postgres app to prevent psycopg import
    DJANGO_APPS = (
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
        # "django.contrib.postgres",  # excluded for tests
        "django.contrib.sessions",
        "django.contrib.staticfiles",
    )

    # clear third-party apps to avoid missing dependencies in test environment
    THIRD_PARTY_APPS = ()

    # minimal installed apps: django contrib required plus common/core/owasp
    INSTALLED_APPS = (
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.staticfiles",
        "apps.common",
        "apps.core",
        "apps.owasp",
        "apps.github",
    )

    # avoid requiring custom user model
    AUTH_USER_MODEL = "auth.User"
