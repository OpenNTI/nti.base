#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import is_not
from hamcrest import assert_that
does_not = is_not

import unittest

from nti.base._compat import bytes_
from nti.base._compat import unicode_

from nti.base.tests import SharedConfiguringTestLayer


class TestCompat(unittest.TestCase):

    layer = SharedConfiguringTestLayer

    def test_bytes(self):
        assert_that(bytes_(u'\u2019'), is_('\xe2\x80\x99'))
        assert_that(unicode_('\xe2\x80\x99'), is_(u'\u2019'))
