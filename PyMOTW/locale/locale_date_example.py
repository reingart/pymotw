#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
#
"""Print dates in locale-specfic format.
"""
#end_pymotw_header

import locale
import time

sample_locales = [ ('USA',      'en_US'),
                   ('Argentina','es_AR'),
                   ('Spain',    'es_ES'),
                   ('Brazil',   'pt_BR'),
                   ('Mexico',   'es_MX'),
                   ]

for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)
    print '%20s: %s' % (name, time.strftime(locale.nl_langinfo(locale.D_T_FMT)))
