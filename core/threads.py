import logging
import threading

import sys

from libs import Leap
from core.listeners import LeapListener

class LeapMotionListenerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        # set this thread as a daemon to terminate when the
        # main program terminates.
        # self.daemon = True

    def run(self):
        try:
            listener = LeapListener()
            controller = Leap.Controller()
            controller.set_policy_flags(Leap.Controller.POLICY_BACKGROUND_FRAMES)

            controller.add_listener(listener)

            sys.stdin.readline()

        except Exception as e:
            logging.error(e);

        finally:
            controller.remove_listener(listener)
