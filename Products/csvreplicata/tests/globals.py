#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
"""
Globals to use in tests.


Lot of files generated by the collective.generic packages  will try to load user defined objects in user specific files.
The final goal is to regenerate easyly the test infrastructure on templates updates without impacting
user-specific test boilerplate.
We do not use paster local commands (insert/update) as it cannot determine witch is specific or not and we prefer to totally
separe generated stuff and what is user specific



If you need to edit something in this file, you must have better to do it in:


    - user_globals.py

All from there will be imported in this namespace

"""
################################################################################

import ConfigParser
import os
import re
import sys
from copy import deepcopy
from pprint import pprint
cwd = os.path.dirname(__file__)
try:import zope
except:pass
try:from zope.interface.verify import verifyObject
except:pass

try:from zope import interface, schema
except:pass
try:from zope.component import adapts, getMultiAdapter, getAdapter, getAdapters
except:pass
try:import z3c
except:pass

def get_interfaces(o):
    return [o for o in o.__provides__.interfaces()]

try:from zope.interface import implementedBy, providedBy
except:pass

# used on testing
# copied from ZopeLite Class from zope.testingZope.TestCase
# but we can't import it
# if we do we polluate our os.environment and ZopeTestcase usecase detction
def errprint(msg):
    """Writes 'msg' to stderr and flushes the stream."""
    sys.stderr.write(msg)
    sys.stderr.flush()

def pstriplist(s):
    print '\n'.join([a.rstrip() for a in s.split('\n') if a.strip()])

# load user specific globals
try: from Products.csvreplicata.tests.user_globals import *
except: pass

