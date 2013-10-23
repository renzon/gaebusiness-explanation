# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from user import facade
from log import facade as log_facade
from user.model import User
from zen import router


def index(_write_tmpl, name=None):
    url = router.to_path(index)
    users = User.query_all().fetch()
    if name:
        cmds = log_facade.save_user_log(name)+facade.save_user(name)
        user=cmds.execute().result
        if not cmds.errors:
            users.insert(0, user)
    values = {'form_url': url, 'users': users}
    _write_tmpl('templates/form.html', values)
