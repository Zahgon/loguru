import sys
from sys import exc_info


def get_frame_fallback(n):
    pass


def load_get_frame_function():
    if hasattr(sys, "_getframe"):
        get_frame = sys._getframe
    else:
        get_frame = get_frame_fallback
    return get_frame


get_frame = load_get_frame_function()
