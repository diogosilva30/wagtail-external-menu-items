"""
Imports `WAGTAIL_EXTERNAL_MENU_ITEMS` settings from Django settings
"""
from django.conf import settings as django_settings

from .exceptions import MissingSetting

# Get settings
settings = getattr(django_settings, "WAGTAIL_EXTERNAL_MENU_ITEMS", {})


def get_setting(name: str, required: bool = True):
    setting = settings.get(name, None)

    if setting is None and required:
        raise MissingSetting(name)
    return setting