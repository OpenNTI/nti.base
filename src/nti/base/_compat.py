#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import six
import inspect

PY2 = six.PY2
PY3 = six.PY3

text_type = six.text_type
binary_type = six.binary_type
class_types = six.class_types
string_types = six.string_types
integer_types = six.integer_types

logger = __import__('logging').getLogger(__name__)


def bytes_(s, encoding='utf-8', errors='strict'):
    """
    If ``s`` is an instance of ``text_type``, return
    ``s.encode(encoding, errors)``, otherwise return ``s``
    """
    if isinstance(s, six.text_type):
        return s.encode(encoding, errors)
    return s


def text_(s, encoding='utf-8', err='strict'):
    """
    Decode a byte sequence and unicode result
    """
    s = s.decode(encoding, err) if isinstance(s, bytes) else s
    return six.text_type(s) if s is not None else None
unicode_ = to_unicode = text_


if PY3:
    def ascii_native_(s):
        if isinstance(s, six.text_type):
            s = s.encode('ascii')
        return str(s, 'ascii', 'strict')
else:
    def ascii_native_(s):
        if isinstance(s, six.text_type):
            s = s.encode('ascii')
        return str(s)


if PY3:
    def native_(s, encoding='latin-1', errors='strict'):
        """ 
        If ``s`` is an instance of ``text_type``, return
        ``s``, otherwise return ``str(s, encoding, errors)``
        """
        if isinstance(s, six.text_type):
            return s
        return str(s, encoding, errors)
else:
    def native_(s, encoding='latin-1', errors='strict'):
        """ 
        If ``s`` is an instance of ``text_type``, return
        ``s.encode(encoding, errors)``, otherwise return ``str(s)``
        """
        if isinstance(s, six.text_type):
            return s.encode(encoding, errors)
        return str(s)


def is_bound_method(ob):
    return inspect.ismethod(ob) \
       and six.get_method_function(ob) is not None


try:
    from inspect import getfullargspec as getargspec
except ImportError:
    from inspect import getargspec


def is_unbound_method(fn):
    """
    This consistently verifies that the callable is bound to a
    class.
    """
    is_bound = is_bound_method(fn)

    if not is_bound and inspect.isroutine(fn):
        spec = getargspec(fn)
        has_self = len(spec.args) > 0 and spec.args[0] == 'self'

        if PY2 and inspect.ismethod(fn):
            return True
        elif inspect.isfunction(fn) and has_self:
            return True

    return False
