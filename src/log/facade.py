# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from log.model import SaveUserLog


def save_user_log(name):
    log = SaveUserLog(user=name)
    log.put()
    return log
