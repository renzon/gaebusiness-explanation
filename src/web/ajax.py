# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
import logging
from user import facade
from user.model import User


def save_user(_resp, name):
    user = facade.save_user(name).execute().result
    js = json.dumps(user.to_dict())
    _resp.write(js)
