# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from user.commands import SaveUserCmd
from user.model import User


def save_user(name):
    return SaveUserCmd(name)
