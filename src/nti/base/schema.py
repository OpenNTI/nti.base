#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id: schema.py 101923 2016-12-05 00:21:48Z carlos.sanchez $
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import numbers

from zope import schema

class Number(schema.Float):
	"""
	A field that parses like a float from a string, but accepts any number.
	"""
	_type = numbers.Number
