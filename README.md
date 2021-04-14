# wagtail-external-menu-items

Add external links to Wagtail Dashboard Menu


# Installation :package:

From PyPi repository:

```
pip install wagtail-external-menu-items
```

From source code:

```
git clone https://github.com/spamz23/wagtail-external-menu-items.git
virtualenv venv
./venv/scripts/activate
pip install -r requirements.txt
```

# Quickstart


1. Add `wagtail_external_menu_items` to your `INSTALLED_APPS` inside Django settings:

```python
INSTALLED_APPS = (
    # ...
    'wagtail_external_menu_items',
)
```


2. Add some configuration settings (inside your Django configs):

```python
# ...

WAGTAIL_EXTERNAL_MENU_ITEMS={
    # A list of dicts, where each dict is a item (button) to add to the dashboard
    "items": [
        {
            "label": "Sentry Logs", # The name of the button
            "url": "https://sentry.io/organizations/your-organization", # The external link
            "classnames": "icon icon-fa-book", # Any classname, in this case we assign a font awesome icon (must have fontawesome installed)
        }
    ],
    "order": 1000 # Optional! The starting order for the items
}
```

That's all the configuration needed!


## Contributing

All pull requests are welcome! In which ways you can provide your awesome contribution?
