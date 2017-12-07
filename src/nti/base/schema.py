#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import numbers
import collections

from zope import schema

from zope.schema.interfaces import TooLong
from zope.schema.interfaces import TooShort
from zope.schema.interfaces import ValidationError
from zope.schema.interfaces import WrongContainedType

logger = __import__('logging').getLogger(__name__)


class FieldValidationMixin(object):
    """
    A field mixin that causes slightly better errors to be created.
    """

    @property
    def __fixup_name__(self):
        """
        The :class:`zope.schema.fieldproperty.FieldPropertyStoredThroughField` class mangles
        the field name; this undoes that mangling.
        """
        if self.__name__ and self.__name__.startswith('__st_') and self.__name__.endswith('_st'):
            return self.__name__[5:-3]
        return self.__name__

    def _fixup_validation_error_args(self, e, value):
        # Called when the exception has one argument, which is usually, though not always,
        # the message
        e.args = (value, e.args[0], self.__fixup_name__)

    def _fixup_validation_error_no_args(self, e, value):
        # Called when there are no arguments
        e.args = (value, str(e), self.__fixup_name__)

    def _reraise_validation_error(self, e, value, _raise=False):
        if len(e.args) == 1:  # typically the message is the only thing
            self._fixup_validation_error_args(e, value)
        elif len(e.args) == 0:  # Typically a SchemaNotProvided. Grr.
            self._fixup_validation_error_no_args(e, value)
        elif isinstance(e, TooShort) and len(e.args) == 2:
            e.args = (self.__fixup_name__.capitalize() + ' is too short.',
                      self.__fixup_name__,
                      value)
        elif isinstance(e, TooLong) and len(e.args) == 2:
            e.args = (self.__fixup_name__.capitalize() + ' is too long.',
                      self.__fixup_name__,
                      value)
        e.field = self
        if not getattr(e, 'value', None):
            e.value = value
        if _raise:
            raise e
        raise  # pylint: disable=misplaced-bare-raise

    def _validate(self, value):
        try:
            super(FieldValidationMixin, self)._validate(value)
        except WrongContainedType as e:
            # args[0] will either be a list of Exceptions or a list of tuples, (name, exception),
            # depending who did the validating (dm.zope.schema doing the later)
            if e.args and isinstance(e.args[0], collections.Iterable):
                e.errors = [
                    arg[1] if isinstance(arg, tuple) else arg for arg in e.args[0]
                ]
            e.value = value
            e.field = self
            raise
        except ValidationError as e:
            self._reraise_validation_error(e, value)


class Number(FieldValidationMixin, schema.Float):
    """
    A field that parses like a float from a string, but accepts any number.
    """
    _type = numbers.Number
