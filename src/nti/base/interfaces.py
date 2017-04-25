#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id: interfaces.py 96516 2016-09-09 14:55:16Z carlos.sanchez $
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.base.schema import Number


class ICreatedTime(interface.Interface):
    """
    Something that (immutably) tracks its created time.
    """

    createdTime = Number(title=u"The timestamp at which this object was created.",
                         description=u"Typically set automatically by the object.",
                         default=0.0)


class ILastModified(ICreatedTime):
    """
    Something that tracks a modification timestamp.
    """

    lastModified = Number(title=u"The timestamp at which this object or its contents was last modified.",
                          default=0.0)


class ICreated(interface.Interface):
    """
    Something created by an identified entity.
    """
    creator = interface.Attribute(u"The creator of this object.")


class ILastViewed(ILastModified):
    """
    In addition to tracking modification and creation times, this
    object tracks viewing (or access) times.

    For security sensitive objects, this may be set automatically in
    an audit-log type fashion. The most typical use, however, will be
    to allow clients to track whether or not the item has been
    displayed to the end user since its last modification; in that
    case, the client will be responsible for updating the value seen
    here explicitly (we can not assume that requesting an object for
    externalization, for example, results in viewing).

    In some cases it may be necessary to supplement this object with
    additional information such as a counter to get the desired
    behaviour.
    """
    # There is no zope.dublincore analoge for this.
    lastViewed = Number(title=u"The timestamp at which this object was last viewed.",
                        default=0.0)


class ITitled(interface.Interface):
    """
    A piece of content with a title, either human created or potentially
    automatically generated. (This differs from, say, a person's honorrific title.
    """
    title = interface.Attribute(u"The title of this object.")


class INamed(interface.Interface):
    """
    An item with a filename
    """
    filename = interface.Attribute(u"The filename.")


class IFile(interface.Interface):

    contentType = interface.Attribute(
        u"The content type identifies the type of data.")

    data = interface.Attribute(u"The actual content of the object.")

    def getSize():
        """
        Return the byte-size of the data of the object.
        """


class INamedFile(INamed, IFile):
    pass


class IConstrained(interface.Interface):
    """
    Marker interface for objects that are constrained
    """


class IContentTypeMarker(interface.Interface):
    """
    Marker interface for deriving mimetypes from class names.
    """
