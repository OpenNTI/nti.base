#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import six

from zope.interface import Attribute
from zope.interface import Interface
from zope.interface import classImplements

from nti.base.schema import Number


class ICreatedTime(Interface):
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


class ICreated(Interface):
    """
    Something created by an identified entity.
    """
    creator = Attribute(u"The creator of this object.")


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


class ITitled(Interface):
    """
    A piece of content with a title, either human created or potentially
    automatically generated. (This differs from, say, a person's honorrific title.
    """
    title = Attribute(u"The title of this object.")


class ITitledDescribed(ITitled):
    """
    A piece of content with a title and description
    """
    description = Attribute(u"The human-readable description of this object.")


class INamed(Interface):
    """
    An item with a filename
    """
    filename = Attribute(u"The filename.")


class IFile(Interface):

    contentType = Attribute(u"The content type identifies the type of data.")

    data = Attribute(u"The actual content of the object.")

    def getSize():
        """
        Return the byte-size of the data of the object.
        """


class INamedFile(INamed, IFile):
    pass


class IConstrained(Interface):
    """
    Marker interface for objects that are constrained
    """


class IContentTypeMarker(Interface):
    """
    Marker interface for deriving mimetypes from class names.
    """


# builtins

try:
    from nti.contentfragments.interfaces import IBytes
    from nti.contentfragments.interfaces import IString
    from nti.contentfragments.interfaces import IUnicode
except ImportError:
    class IBytes(Interface):
        """
        Marker interface for bytes.
        """
    classImplements(bytes, IBytes)

    class IString(Interface):
        """
        Marker interface for mutable strings.
        """
    classImplements(str, IString)

    class IUnicode(Interface):
        """
        Marker interface for mutable unicode strings.
        """

    if six.PY3:
        classImplements(str, IUnicode)
    else:
        classImplements(unicode, IUnicode)


class INumeric(Interface):
    """
    Marker interface for a numeric value.
    """
classImplements(int, INumeric)
classImplements(float, INumeric)

if six.PY2:
    classImplements(long, INumeric)


class IBoolean(Interface):
    """
    Marker interface for a boolean.
    """
classImplements(bool, IBoolean)


class IIterable(Interface):
    """
    Base interface for iterable types.
    """

    def __iter__():
        """Return an iterator object.
        """


class IList(IIterable):
    """
    Marker interface for lists
    """
classImplements(list, IList)


class ITuple(IIterable):
    """
    Marker interface for immutable lists
    """
classImplements(tuple, ITuple)


class IDict(IIterable):
    """
    Marker interface for dicts
    """

    def items():
        """
        Returns an iterable list of couples key - value,
        as a list of tuples.
        """

    def values():
        """
        Returns an iterable list of the dict values.
        """

    def keys():
        """
        Returns an iterable list of the dict keys.
        """

    def __contains__(key):
        """
        Returns a boolean, True if the key exists in the dict,
        False otherwise.
        """
classImplements(dict, IDict)


class IFileIO(Interface):
    """
    Defines an python file builtin.
    """

    def seek(offset, whence=0):
        """
        Set the file's current position.
        """

    def read(size):
        """
        Read at most size bytes from the file.
        """

    def readline(length=None):
        """
        Read one entire line from the file.
        """

    def readlines(sizehint=0):
        """
        Read until EOF using readline() and return a list
        containing the lines thus read.
        """

    def write(s):
        """
        Write a string to the file.
        """

    def writelines(iterable):
        """
        Write a sequence of strings to the file.
        """

    def tell():
        """
        Return the file's current position.
        """

    def truncate(size=None):
        """
        Truncate the file's size.
        """


if six.PY3:
    from io import FileIO, StringIO, TextIOWrapper, BytesIO
    classImplements(FileIO, IFileIO)
    classImplements(BytesIO, IFileIO)
    classImplements(StringIO, IFileIO)
    classImplements(TextIOWrapper, IFileIO)
else:
    classImplements(file, IFileIO)
