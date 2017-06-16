#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import assert_that

import unittest

from zope.schema.interfaces import SchemaNotProvided

from nti.base.schema import FieldValidationMixin

from nti.base.tests import NTIBaseLayer


class TestSchema(unittest.TestCase):

    layer = NTIBaseLayer

    def _getTargetClass(self):
        from nti.base.schema import Number
        return Number

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_class_conforms_to_IFloat(self):
        from zope.interface.verify import verifyClass
        from zope.schema.interfaces import IFloat
        verifyClass(IFloat, self._getTargetClass())

    def test_instance_conforms_to_IFloat(self):
        from zope.interface.verify import verifyObject
        from zope.schema.interfaces import IFloat
        verifyObject(IFloat, self._makeOne())

    def test_validate_not_required(self):
        field = self._makeOne(required=False)
        field.validate(None)
        field.validate(10.0)
        field.validate(10)
        field.validate(0)
        field.validate(1000.0003)
        
    def test_one_arg(self):
        field = FieldValidationMixin()
        field.__name__ = 'foo'

        ex = SchemaNotProvided('msg')
        try:
            field._reraise_validation_error(ex, 'value', _raise=True)
        except SchemaNotProvided:
            assert_that(ex.args, is_(('value', 'msg', 'foo')))

    def test_no_arg(self):
        field = FieldValidationMixin()
        field.__name__ = 'foo'

        ex = SchemaNotProvided()
        try:
            field._reraise_validation_error(ex, 'value', _raise=True)
        except SchemaNotProvided:
            assert_that(ex.args, is_(('value', '', 'foo')))
