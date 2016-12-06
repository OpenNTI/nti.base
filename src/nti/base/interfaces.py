#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id: interfaces.py 96516 2016-09-09 14:55:16Z carlos.sanchez $
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

from zope import interface

class ICreatedTime(interface.Interface):
	"""
	Something that (immutably) tracks its created time.
	"""

	createdTime = interface.Attribute(u"The timestamp at which this object was created.")

class ILastModified(ICreatedTime):
	"""
	Something that tracks a modification timestamp.
	"""

	lastModified = interface.Attribute("The timestamp at which this object or its contents was last modified.")

class ICreated(interface.Interface):
	"""
	Something created by an identified entity.
	"""
	creator = interface.Attribute("The creator of this object.")

class ITitled(interface.Interface):
	"""
	A piece of content with a title, either human created or potentially
	automatically generated. (This differs from, say, a person's honorrific title.
	"""
	title = interface.Attribute("The title of this object.")
