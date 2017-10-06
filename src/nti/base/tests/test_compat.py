#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import is_not
from hamcrest import assert_that
does_not = is_not

import six
import unittest

from nti.base._compat import text_
from nti.base._compat import bytes_
from nti.base._compat import native_
from nti.base._compat import ascii_native_


class TestCompat(unittest.TestCase):

    def test_bytes(self):
        assert_that(bytes_(u'\u2019'), is_(b'\xe2\x80\x99'))
        assert_that(text_(b'\xe2\x80\x99'), is_(u'\u2019'))

    def test_ascii_native(self):
        assert_that(ascii_native_(u'ichigo'), is_('ichigo'))
        assert_that(ascii_native_('aizen'), is_('aizen'))

    def test_native(self):
        if six.PY2:
            assert_that(native_(u'こんにちは ichigo', 'utf-8'),
                        is_('\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf ichigo'))
        else:  # pragma: no cover
            assert_that(native_(u'こんにちは ichigo', 'utf-8'),
                        is_(u'こんにちは ichigo'))

        assert_that(native_(b'ichigo', 'utf-8'),
                    is_(u'ichigo'))
