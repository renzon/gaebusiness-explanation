# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import Command
from log.model import SaveUserLog


class SaveUserLogCmd(Command):
    def __init__(self, name):
        Command.__init__(self, name=name)

    def do_business(self, stop_on_error=True):
        if not self.name:
            self.add_error('name', 'Name is required')
        else:
            self.result = SaveUserLog(user=self.name)

    def commit(self):
        return self.result
