# Python 2/3 compatibility.
from __future__ import print_function

import sys
from threading import Event

from plover import log
from plover.oslayer.keyboardcontrol import KeyboardEmulation

from plover.gui_none.engine import Engine


def show_error(title, message):
    print('%s: %s' % (title, message))


def main(config):

    engine = Engine(config, KeyboardEmulation())
    if not engine.load_config():
        return 3
    quitting = Event()
    engine.hook_connect('quit', quitting.set)
    engine.start()
    try:
        quitting.wait()
    except KeyboardInterrupt:
        pass
    engine.quit()
    engine.join()

    return 0
