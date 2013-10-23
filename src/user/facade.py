# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from user.model import User


def save_user(name):
    user = User(name=name)
    user.put()
    logging.info("Saving %s" % user)
    return user
