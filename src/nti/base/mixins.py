#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import time

from zope import interface

from nti.base.interfaces import INamedFile
from nti.base.interfaces import ICreatedTime
from nti.base.interfaces import ILastModified

logger = __import__('logging').getLogger(__name__)


@interface.implementer(ICreatedTime)
class CreatedTimeMixin(object):

    _SET_CREATED_MODTIME_ON_INIT = True

    createdTime = 0

    def __init__(self, *args, **kwargs):
        if self._SET_CREATED_MODTIME_ON_INIT and self.createdTime == 0:
            self.createdTime = time.time()
        super(CreatedTimeMixin, self).__init__(*args, **kwargs)


class ModifiedTimeMixin(object):

    lastModified = 0

    # pylint: disable=useless-super-delegation
    def __init__(self, *args, **kwargs):
        super(ModifiedTimeMixin, self).__init__(*args, **kwargs)

    def updateLastMod(self, t=None):
        self.lastModified = (t if t is not None and t > self.lastModified else time.time())
        return self.lastModified

    def updateLastModIfGreater(self, t):
        """
        Only if the given time is (not None and) greater than this object's is this object's time changed.
        """
        if t is not None and t > self.lastModified:
            self.lastModified = t
        return self.lastModified


@interface.implementer(ILastModified)
class CreatedAndModifiedTimeMixin(CreatedTimeMixin, ModifiedTimeMixin):

    def __init__(self, *args, **kwargs):
        # We set the times now so subclasses can rely on them
        if self._SET_CREATED_MODTIME_ON_INIT:
            self.createdTime = time.time()
            self.updateLastModIfGreater(self.createdTime)
        super(CreatedAndModifiedTimeMixin, self).__init__(*args, **kwargs)


@interface.implementer(INamedFile)
class FileMixin(CreatedAndModifiedTimeMixin):

    # pylint: disable=keyword-arg-before-vararg
    def __init__(self, contentType='', filename=None, *args, **kwargs):
        self.filename = filename
        self.contentType = contentType
        super(FileMixin, self).__init__(*args, **kwargs)
        
    @property
    def length(self):
        return self.getSize()

    def getSize(self):
        raise NotImplementedError()
