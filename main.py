#!/usr/bin/python

from core.threads import LeapMotionListenerThread
def main():
    leap_thread = LeapMotionListenerThread()
    leap_thread.start()

if __name__ == "__main__":
    main()