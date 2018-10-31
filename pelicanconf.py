#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Blerim Emruli'
SITENAME = 'Random ramblings of Blerim Emruli'
SITESUBTITLE = u'Musings and ramblings through the world of Python and beyond'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/Stockholm'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#MARKUP = ('md', 'ipynb')
#PLUGINS = ['ipynb.markup']

MARKUP = ['md']
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = [
    'series',  # enabling to have a series of post that are linked together
    'summary',       # auto-summarizing articles
    'feed_summary',  # use summaries for RSS, not full articles
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal'
]
IGNORE_FILES = ['.ipynb_checkpoints']


# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# THEME SETTINGS
THEME = './theme/'

ABOUT_PAGE = '/pages/about.html'

LINKEDIN_ADDRESS = 'https://www.linkedin.com/in/eblerim/'
GITHUB_USERNAME = 'eblerim'
STACKOVERFLOW_ADDRESS = 'https://stackoverflow.com/users/7378394/eblerim'
# TWITTER_USERNAME = ''
AUTHOR_BLOG = 'http://eblerim.github.io'
AUTHOR_WEBSITE = 'http://forskning.mah.se/en/id/ai2686'
# AUTHOR_CV = "http://staff.washington.edu/jakevdp/media/pdfs/CV.pdf"

SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']

# Footer info

LICENSE_URL = "https://github.com/eblerim/eblerim.github.io-source/blob/master/LICENSE"
LICENSE = "MIT"