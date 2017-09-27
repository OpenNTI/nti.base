#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import has_length
from hamcrest import assert_that
from hamcrest import has_property

import unittest

from zope import schema

from zope.schema.interfaces import ValidationError
from zope.schema.interfaces import SchemaNotProvided
from zope.schema.interfaces import WrongContainedType

from nti.base.schema import FieldValidationMixin


class TestSchema(unittest.TestCase):

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

    def test_wrong_contained_type(self):
        class WCT(schema.Float):
            def _validate(self, value):
                raise WrongContainedType(("Invalid value",), value)

        class Invalid(FieldValidationMixin, WCT):
            pass
        n = Invalid()
        with self.assertRaises(WrongContainedType) as e:
            n._validate(100)
            assert_that(e, has_property('errors', has_length(1)))

    def test_validation_error(self):
        class ValError(schema.Float):
            def _validate(self, value):
                raise ValidationError("Invalid value", value)

        class Invalid(FieldValidationMixin, ValError):
            pass
        n = Invalid()
        with self.assertRaises(ValidationError):
            n._validate(100)
