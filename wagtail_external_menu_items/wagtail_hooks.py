"""
Wagtail hooks to register the items
"""

from wagtail.core import hooks
from wagtail.admin.menu import MenuItem


from .settings import get_setting

ITEMS = get_setting("items")
ORDER = get_setting("order", required=False) or 1000


def parse_url(url: str) -> str:
    """
    Makes sure the URL starts with 'http://'
    """
    # Replace HTTPS with HTTP (if exists)
    url = url.replace("https://", "http://")

    if url.startswith("http://"):
        return url

    return f"http://{url}"


def get_lazy_menu_item(menu_item: dict) -> callable:
    """
    Creates a lazy `MenuItem` object.
    """
    return lambda: MenuItem(
        label=menu_item["label"],
        url=parse_url(menu_item["url"]),
        classnames=menu_item["classnames"],
        order=ORDER,
    )


# Register the items in the Wagtail Dashboard
for item in ITEMS:
    hooks.register(
        "register_admin_menu_item",
        get_lazy_menu_item(item),
    )