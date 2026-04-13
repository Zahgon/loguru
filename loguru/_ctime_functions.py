import os


def load_ctime_functions():
    if os.name == "nt":
        import win32_setctime

        def get_ctime_windows(filepath):
            pass

        def set_ctime_windows(filepath, timestamp):
            pass

        return get_ctime_windows, set_ctime_windows

    if hasattr(os.stat_result, "st_birthtime"):

        def get_ctime_macos(filepath):
            pass

        def set_ctime_macos(filepath, timestamp):
            pass

        return get_ctime_macos, set_ctime_macos

    if hasattr(os, "getxattr") and hasattr(os, "setxattr"):

        def get_ctime_linux(filepath):
            pass

        def set_ctime_linux(filepath, timestamp):
            pass

        return get_ctime_linux, set_ctime_linux

    def get_ctime_fallback(filepath):
        pass

    def set_ctime_fallback(filepath, timestamp):
        pass

    return get_ctime_fallback, set_ctime_fallback


get_ctime, set_ctime = load_ctime_functions()
