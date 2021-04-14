"""
Wagtail hooks to register the items
"""

from wagtail.core import hooks
from wagtail.admin.menu import MenuItem


from .settings import get_setting

ITEMS = get_setting("items")
ORDER = get_setting("order", required=False) or 1000


def get_lazy_menu_item(item):
    """
    Creates a lazy `MenuItem` object.
    """
    return (
        lambda: MenuItem(
            label=item["label"],
            url=item["url"],
            classnames=item["classnames"],
            order=ORDER,
        ),
    )


def main():
    """
    Register the items in the Wagtail Dashboard
    """
    for item in ITEMS:
        hooks.register(
            "register_admin_menu_item",
            get_lazy_menu_item(item),
        )


if __name__ == "__main__":
    main()