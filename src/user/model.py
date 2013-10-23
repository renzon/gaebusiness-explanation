# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb


class User(ndb.Model):
    name = ndb.StringProperty(required=True)

    @classmethod
    def query_all(cls):
        return cls.query().order(cls.name)
