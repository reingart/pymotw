#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import sys

print('Version info:')
print('')
print('sys.version      = %s' % repr(sys.version))
print('sys.version_info = %s' % repr(sys.version_info))
print('sys.hexversion   = %s' % hex(sys.hexversion))
if sys.version_info[0] < 3:
    print('sys.subversion   = %s' % repr(sys.subversion))
print('sys.api_version  = %s' % sys.api_version)
