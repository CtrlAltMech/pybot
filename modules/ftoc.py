# -*- coding: utf-8 -*-

##Converts farenheit to celcius##

import sys
from event import Event

if sys.version_info > (3, 0, 0):
    try:
        from .basemodule import BaseModule
    except (ImportError, SystemError):
        from modules.basemodule import BaseModule
else:
    try:
        from basemodule import BaseModule
    except (ImportError, SystemError):
        from modules.basemodule import BaseModule


class Ftoc(BaseModule):
    def post_init(self):
        ftoc = Event("__.ftoc__")
        ftoc.define(msg_definition="^\\.ftoc")
        ftoc.subscribe(self)
        self.cmd = ".ftoc"
        self.help = ".ftoc [farenheit]"

        self.bot.register_event(ftoc, self)

    def handle(self, event):
        try:
            if event.msg.startswith(".ftoc"):
                # Splits the command from the number ['.ftoc', '<some number>']
                split_msg = event.msg.split()
                f_temp = split_msg[1]
                f = float(f_temp)
                # Does math to convert from freedom units to celcius
                c = (f - 32) * (.5555)
                # Spits it out in the proper channel
                self.say(event.channel, str(round(c, 1)) + "° C")

        except ValueError:
            self.say(event.channel, "Enter a number you rube!")
        except IndexError:
            self.say(event.channel, "Try '.ftoc [farenheit]'")
