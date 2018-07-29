#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://alfonso-pinto.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

FOOTER_LINKS = (('Source', 'https://github.com/Elhodred/Elhodred.github.io-src'),
                ('RSS', SITEURL + '/feeds/all.atom.xml'),
                ('Pelican', 'http://blog.getpelican.com/'),
                ('PurePelican (fork)', 'https://github.com/Elhodred/pure'),)
# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
