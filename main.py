#!/usr/bin/python
#
import sys
import logging

from libs import Leap
from core.listeners import LeapListener

def main():
    # leap_thread = LeapMotionListenerThread()
    # leap_thread.start()

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

if __name__ == "__main__":
    main()