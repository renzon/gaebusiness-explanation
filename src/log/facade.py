# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from log.commands import SaveUserLogCmd
from log.model import SaveUserLog


def save_user_log(name):
    return SaveUserLogCmd(name)
