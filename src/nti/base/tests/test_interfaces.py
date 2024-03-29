#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods

from hamcrest import is_
from hamcrest import is_not
from hamcrest import contains
from hamcrest import assert_that
from hamcrest import has_property
does_not = is_not

import unittest

from zope import interface

from nti.base.interfaces import IDict
from nti.base.interfaces import IList
from nti.base.interfaces import IBytes
from nti.base.interfaces import ITuple
from nti.base.interfaces import IFileIO
from nti.base.interfaces import IBoolean
from nti.base.interfaces import INumeric
from nti.base.interfaces import IUnicode
from nti.base.interfaces import IIterable
from nti.base.interfaces import IBasestring


class TestInterfaces(unittest.TestCase):

    def test_dolmen_builtins(self):
        sample = b"Tis' a very nice string."
        assert_that(IBytes.providedBy(sample), is_(True))

        sample = u"Aye, indeed my friend."
        assert_that(IUnicode.providedBy(sample), is_(True))
        assert_that(IBasestring.providedBy(sample), is_(True))

        sample = "Small fire."
        assert_that(IBasestring.providedBy(sample), is_(True))

        sample = True
        assert_that(IBoolean.providedBy(sample), is_(True))

        sample = 1
        assert_that(INumeric.providedBy(sample), is_(True))

        sample = 0.1
        assert_that(INumeric.providedBy(sample), is_(True))

        sample = ('MacBeth', 'Lady MacBeth')
        assert_that(ITuple.providedBy(sample), is_(True))
        assert_that(IIterable.providedBy(sample), is_(True))

        sample = ['Banco', 'Duncan']
        assert_that(IList.providedBy(sample), is_(True))
        assert_that(IIterable.providedBy(sample), is_(True))

        sample = {"Glamis": "MacBeth", "Fife": "MacDuff"}
        assert_that(IDict.providedBy(sample), is_(True))
        assert_that(IIterable.providedBy(sample), is_(True))

        sample = open(__file__, 'r')
        assert_that(IFileIO.providedBy(sample), is_(True))
        sample.close()

    def test_fileio(self):
        from io import FileIO, StringIO, TextIOWrapper, BytesIO, BufferedRWPair
        for cls in (FileIO, StringIO, TextIOWrapper, BytesIO, BufferedRWPair):
            spec = interface.implementedBy(cls)
            assert_that(spec,
                        has_property('__bases__'), contains(IFileIO))
