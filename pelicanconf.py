#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Diego Fainstein'
SITENAME = 'Laboratorio de Bioingeniería - CIC'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Argentina/Buenos_Aires'
DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('CIC La Plata', 'http://ciclaplata.org.ar/'),
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/CICCONICETUNLP?fref=ts'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'pdfs']

# THEME = "../pelican-elegant-1.3"
# THEME = "../pelican-themes/notmyidea-cms"    # es un tema built-in
# THEME = "../pelican-themes/foundation-default-colours"
THEME = "../pelican-themes/alchemy/alchemy"
