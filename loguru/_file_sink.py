import datetime
import decimal
import glob
import numbers
import os
import shutil
import string
from functools import partial
from stat import ST_DEV, ST_INO

from . import _string_parsers as string_parsers
from ._ctime_functions import get_ctime, set_ctime
from ._datetime import aware_now


def generate_rename_path(root, ext, creation_time):
    pass


class FileDateFormatter:
    def __init__(self, datetime=None):
        self.datetime = datetime or aware_now()

    def __format__(self, spec):
        if not spec:
            spec = "%Y-%m-%d_%H-%M-%S_%f"
        return self.datetime.__format__(spec)


class Compression:
    @staticmethod
    def add_compress(path_in, path_out, opener, **kwargs):
        pass

    @staticmethod
    def write_compress(path_in, path_out, opener, **kwargs):
        pass

    @staticmethod
    def copy_compress(path_in, path_out, opener, **kwargs):
        pass

    @staticmethod
    def compression(path_in, ext, compress_function):
        pass


class Retention:
    @staticmethod
    def retention_count(logs, number):
        pass

    @staticmethod
    def retention_age(logs, seconds):
        pass


class Rotation:
    @staticmethod
    def forward_day(t):
        pass

    @staticmethod
    def forward_weekday(t, weekday):
        pass

    @staticmethod
    def forward_interval(t, interval):
        pass

    @staticmethod
    def rotation_size(message, file, size_limit):
        pass

    class RotationTime:
        def __init__(self, step_forward, time_init=None):
            self._step_forward = step_forward
            self._time_init = time_init
            self._limit = None

        def __call__(self, message, file):
            record_time = message.record["time"]

            if self._limit is None:
                filepath = os.path.realpath(file.name)
                creation_time = get_ctime(filepath)
                set_ctime(filepath, creation_time)
                start_time = datetime.datetime.fromtimestamp(
                    creation_time, tz=datetime.timezone.utc
                )

                time_init = self._time_init

                if time_init is None:
                    limit = start_time.astimezone(record_time.tzinfo).replace(tzinfo=None)
                    limit = self._step_forward(limit)
                else:
                    tzinfo = record_time.tzinfo if time_init.tzinfo is None else time_init.tzinfo
                    limit = start_time.astimezone(tzinfo).replace(
                        hour=time_init.hour,
                        minute=time_init.minute,
                        second=time_init.second,
                        microsecond=time_init.microsecond,
                    )

                    if limit <= start_time:
                        limit = self._step_forward(limit)

                    if time_init.tzinfo is None:
                        limit = limit.replace(tzinfo=None)

                self._limit = limit

            if self._limit.tzinfo is None:
                record_time = record_time.replace(tzinfo=None)

            if record_time >= self._limit:
                while self._limit <= record_time:
                    self._limit = self._step_forward(self._limit)
                return True
            return False

    class RotationGroup:
        def __init__(self, rotations) -> None:
            self._rotations = rotations

        def __call__(self, message, file) -> bool:
            return any(rotation(message, file) for rotation in self._rotations)


class FileSink:
    def __init__(
        self,
        path,
        *,
        rotation=None,
        retention=None,
        compression=None,
        delay=False,
        watch=False,
        mode="a",
        buffering=1,
        encoding="utf8",
        **kwargs
    ):
        self.encoding = encoding

        self._kwargs = {**kwargs, "mode": mode, "buffering": buffering, "encoding": self.encoding}
        self._path = str(path)

        self._glob_patterns = self._make_glob_patterns(self._path)
        self._rotation_function = self._make_rotation_function(rotation)
        self._retention_function = self._make_retention_function(retention)
        self._compression_function = self._make_compression_function(compression)

        self._file = None
        self._file_path = None

        self._watch = watch
        self._file_dev = -1
        self._file_ino = -1

        if not delay:
            path = self._create_path()
            self._create_dirs(path)
            self._create_file(path)

    def write(self, message):
        pass

    def stop(self):
        pass

    def tasks_to_complete(self):
        pass

    def _create_path(self):
        pass

    def _create_dirs(self, path):
        pass

    def _create_file(self, path):
        pass

    def _close_file(self):
        pass

    def _reopen_if_needed(self):
        # Implemented based on standard library:
        # https://github.com/python/cpython/blob/cb589d1b/Lib/logging/handlers.py#L486
        pass

    def _terminate_file(self, *, is_rotating=False):
        pass

    @staticmethod
    def _make_glob_patterns(path):
        pass

    @staticmethod
    def _make_rotation_function(rotation):
        pass

    @staticmethod
    def _make_retention_function(retention):
        pass

    @staticmethod
    def _make_compression_function(compression):
        pass
