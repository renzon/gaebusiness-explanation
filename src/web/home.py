# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from user.model import User
from zen import router


def index(_write_tmpl, name=None):
    url = router.to_path(index)
    users = User.query_all().fetch()
    if name:
        user = User(name=name)
        user.put()
        users.insert(0, user)
    values = {'form_url': url, 'users': users}
    _write_tmpl('templates/form.html', values)
