#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import none
from hamcrest import is_not
from hamcrest import has_entry
from hamcrest import assert_that
from hamcrest import has_property
does_not = is_not

import sys
import unittest

from nti.base.deprecation import moved

from nti.base.tests import NTIBaseLayer


class TestDeprecation(unittest.TestCase):

    layer = NTIBaseLayer

    def test_moved(self):
        old = moved('nti.base.oldmixins', 'nti.base.mixins')
        assert_that(old, is_not(none()))
        assert_that(old, has_property('CreatedTimeMixin', is_not(none())))
        assert_that(sys.modules, has_entry('nti.base.oldmixins', is_(old)))
        # check import
        __import__('nti.base.oldmixins')
