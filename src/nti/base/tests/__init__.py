#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods,arguments-differ

from zope.component.testlayer import ZCMLFileLayer

import nti.base

NTIBaseLayer = ZCMLFileLayer(nti.base, 'configure.zcml')
