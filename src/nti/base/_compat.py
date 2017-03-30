#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id: _compat.py 103172 2016-12-22 14:53:57Z carlos.sanchez $
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import six

PY3 = six.PY3

text_type = six.text_type
class_types = six.class_types
string_types = six.string_types
integer_types = six.integer_types

if PY3:  # pragma: no cover
    _unicode = lambda s: s
else:
    _unicode = unicode

def bytes_(s, encoding='utf-8', errors='strict'):
    """
    If ``s`` is an instance of ``text_type``, return
    ``s.encode(encoding, errors)``, otherwise return ``str(s)``
    """
    if isinstance(s, text_type):
        return s.encode(encoding, errors)
    return s
native_ = bytes_


def unicode_(s, encoding='utf-8', err='strict'):
    """
    Decode a byte sequence and unicode result
    """
    s = s.decode(encoding, err) if isinstance(s, bytes) else s
    return _unicode(s) if s is not None else None
to_unicode = unicode_
