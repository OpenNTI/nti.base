#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import numbers

from zope import schema

logger = __import__('logging').getLogger(__name__)


class Number(schema.Float):
    """
    A field that parses like a float from a string, but accepts any number.
    """
    _type = numbers.Number
