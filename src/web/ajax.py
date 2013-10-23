# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from user.model import User


def save_user(_resp, name):
    user = User(name=name)
    user.put()
    js = json.dumps(user.to_dict())
    _resp.write(js)