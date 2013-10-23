# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb


class SaveUserLog(ndb.Model):
    creation = ndb.DateTimeProperty(auto_now_add=True)
    user = ndb.StringProperty(required=True)
