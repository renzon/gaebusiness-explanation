# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import Command
from user.model import User


class SaveUserCmd(Command):
    def __init__(self, name):
        Command.__init__(self, name=name)

    def do_business(self, stop_on_error=True):
        self.result = User(name=self.name)

    def commit(self):
        return self.result


