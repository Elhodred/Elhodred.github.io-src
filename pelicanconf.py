#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alfonso Pinto'
AUTHOR_EMAIL = 'alfonso.pinto@gmail.com'
ABOUT_AUTHOR = 'Developer'
SITENAME = "Alfonso Pinto's Notebook"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

THEME = "themes/pure"

STATIC_PATHS = ['images', 'assets']

COVER_IMG_URL = "/images/sidebar.png"
PROFILE_IMAGE_URL = "/images/profile.jpg"
TAGLINE = "A Developer's journey"

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'tipue_search']

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ('github', 'https://github.com/Elhodred'),
    ('twitter', 'https://twitter.com/Elhodred'),
    ('facebook', 'https://www.facebook.com/elhodred'),
)

FOOTER_LINKS = (('Source', 'https://github.com/Elhodred/Elhodred.github.io-src'),
                ('RSS', SITEURL + '/feeds/all.atom.xml'),
                ('Pelican', 'http://blog.getpelican.com/'),
                ('PurePelican (fork)', 'https://github.com/Elhodred/pure'),)

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
        ('About', 'about/'),
)

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
