#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods,unused-variable

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
from nti.base.deprecation import deprecated
from nti.base.deprecation import hides_warnings


class TestDeprecation(unittest.TestCase):

    def test_moved(self):
        old = moved('nti.base.oldmixins', 'nti.base.mixins')
        assert_that(old, is_not(none()))
        assert_that(old, has_property('CreatedTimeMixin', is_not(none())))
        assert_that(sys.modules, has_entry('nti.base.oldmixins', is_(old)))
        # check import
        __import__('nti.base.oldmixins')

        # create modules
        moved('nti.base._a', 'nti.base._b')

    def test_deprecated(self):
        @deprecated()
        class Foo(object):
            pass

        @deprecated()
        def foo():
            pass
        foo()

        class A(object):
            @deprecated()
            def eat(self):
                pass
        A().eat()

    def test_hides_warnings(self):
        @hides_warnings
        def foo():
            pass
        foo()
