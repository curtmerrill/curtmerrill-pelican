#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Curt Merrill'
SITENAME = 'curtmerrill.com'
SITEURL = 'http://localhost:8000'

PATH = 'content'
PAGE_PATHS = ['pages']

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = '%d %B %Y'

DEFAULT_LANG = 'en'

ARTICLE_URL = 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = f'{ARTICLE_URL}index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = f'{PAGE_URL}index.html'

TAG_URL = 'posts/tag/{slug}.html'
TAG_SAVE_AS = f'{TAG_URL}'
TAGS_SAVE_AS = 'posts/tags.html'
YEAR_ARCHIVE_URL = 'posts/{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = f'{YEAR_ARCHIVE_URL}index.html'

DIRECT_TEMPLATES = ['index', 'tags', 'archives']

CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''

DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False

PLUGIN_PATHS = ['./pelican-plugins' ]
PLUGINS = ['assets' ]

# Disable syntax highlighting
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

THEME = 'theme/curtmerrill'
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
