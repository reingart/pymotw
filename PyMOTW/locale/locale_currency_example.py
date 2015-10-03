#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
#
"""Show the same currency value in different formats for different locales.
"""
#end_pymotw_header

import locale

sample_locales = [ ('USA',      'en_US'),
                   ('Argentina','es_AR'),
                   ('Spain',    'es_ES'),
                   ('Brazil',   'pt_BR'),
                   ('Mexico',   'es_MX'),
                   ]

for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)
    print '%20s: %10s  %10s' % (name,
                                locale.currency(1234.56),
                                locale.currency(-1234.56))

