import os

_HERE = os.path.dirname(os.path.abspath(__file__))

AUTHOR = "Daniel Stilck Franca, Tim Möbus"
SITENAME = "TouQan — QuantERA Project"
SITEURL = ""

PATH = os.path.join(_HERE, "content")
OUTPUT_PATH = os.path.join(_HERE, "output")

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "en"
LOCALE = "en_US.UTF-8"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
    ("News", "/category/news.html"),
    ("About", "/pages/summary-of-the-project.html"),
    ("Publications", "/pages/publications.html"),
    ("Principal Investigators", "/pages/principal-investigators.html"),
    ("Contact", "/pages/contact.html"),
)

DISPLAY_PAGES_ON_MENU = False

BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

DEFAULT_PAGINATION = False
DEFAULT_CATEGORY = "News"
USE_FOLDER_AS_CATEGORY = False
SUMMARY_MAX_LENGTH = 40
MENUITEMS = (
    ("News", "/category/news.html"),
    ("About", "/pages/summary-of-the-project.html"),
    ("Publications", "/pages/publications.html"),
    ("Principal Investigators", "/pages/principal-investigators.html"),
    ("Contact", "/pages/contact.html"),
)

ARTICLE_PATHS = ["posts"]
ARTICLE_URL = "posts/{slug}.html"
ARTICLE_SAVE_AS = "posts/{slug}.html"

STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "custom.css"},
    "extra/.nojekyll": {"path": ".nojekyll"},
}
CUSTOM_CSS = "custom.css"

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.attr_list": {},
    },
    "output_format": "html5",
}
DELETE_OUTPUT_DIRECTORY = True

THEME = os.path.join(_HERE, "Flex")

SITELOGO = "/theme/img/profile.png"
SITELOGO_SIZE = 120

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
