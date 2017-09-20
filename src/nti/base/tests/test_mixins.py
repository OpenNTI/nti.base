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
from hamcrest import has_property
does_not = is_not

from nti.testing.matchers import validly_provides
from nti.testing.matchers import verifiably_provides

import time
import unittest

from nti.base.interfaces import ICreatedTime
from nti.base.interfaces import ILastModified

from nti.base.mixins import CreatedAndModifiedTimeMixin


class TestMixins(unittest.TestCase):

    def test_plus_extend(self):
        c = CreatedAndModifiedTimeMixin()
        for iface in (ICreatedTime, ILastModified):
            assert_that(c, validly_provides(iface))
            assert_that(c, verifiably_provides(iface))

        t = time.time() + 100
        c.updateLastMod(t)
        assert_that(c, has_property('lastModified', is_(t)))

        c.updateLastModIfGreater(100)
        assert_that(c, has_property('lastModified', is_(t)))
