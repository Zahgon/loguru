import builtins
import inspect
import io
import keyword
import linecache
import os
import re
import sys
import sysconfig
import tokenize
import traceback

if sys.version_info >= (3, 11):

    def is_exception_group(exc):
        pass

else:
    try:
        from exceptiongroup import ExceptionGroup
    except ImportError:

        def is_exception_group(exc):
            pass

    else:

        def is_exception_group(exc):
            pass


class SyntaxHighlighter:
    _default_style = frozenset(
        {
            "comment": "\x1b[30m\x1b[1m{}\x1b[0m",
            "keyword": "\x1b[35m\x1b[1m{}\x1b[0m",
            "builtin": "\x1b[1m{}\x1b[0m",
            "string": "\x1b[36m{}\x1b[0m",
            "number": "\x1b[34m\x1b[1m{}\x1b[0m",
            "operator": "\x1b[35m\x1b[1m{}\x1b[0m",
            "punctuation": "\x1b[1m{}\x1b[0m",
            "constant": "\x1b[36m\x1b[1m{}\x1b[0m",
            "identifier": "\x1b[1m{}\x1b[0m",
            "other": "{}",
        }.items()
    )

    _builtins = frozenset(dir(builtins))
    _constants = frozenset({"True", "False", "None"})
    _punctuation = frozenset({"(", ")", "[", "]", "{", "}", ":", ",", ";"})

    if sys.version_info >= (3, 12):
        _strings = frozenset(
            {tokenize.STRING, tokenize.FSTRING_START, tokenize.FSTRING_MIDDLE, tokenize.FSTRING_END}
        )
        _fstring_middle = tokenize.FSTRING_MIDDLE
    else:
        _strings = frozenset({tokenize.STRING})
        _fstring_middle = None

    def __init__(self, style=None):
        self._style = style or dict(self._default_style)

    def highlight(self, source):
        pass

    @staticmethod
    def tokenize(source):
        # Worth reading: https://www.asmeurer.com/brown-water-python/
        pass


class ExceptionFormatter:
    _default_theme = frozenset(
        {
            "introduction": "\x1b[33m\x1b[1m{}\x1b[0m",
            "cause": "\x1b[1m{}\x1b[0m",
            "context": "\x1b[1m{}\x1b[0m",
            "dirname": "\x1b[32m{}\x1b[0m",
            "basename": "\x1b[32m\x1b[1m{}\x1b[0m",
            "line": "\x1b[33m{}\x1b[0m",
            "function": "\x1b[35m{}\x1b[0m",
            "exception_type": "\x1b[31m\x1b[1m{}\x1b[0m",
            "exception_value": "\x1b[1m{}\x1b[0m",
            "arrows": "\x1b[36m{}\x1b[0m",
            "value": "\x1b[36m\x1b[1m{}\x1b[0m",
        }.items()
    )

    def __init__(
        self,
        colorize=False,
        backtrace=False,
        diagnose=True,
        theme=None,
        style=None,
        max_length=128,
        encoding="ascii",
        hidden_frames_filename=None,
        prefix="",
    ):
        self._colorize = colorize
        self._diagnose = diagnose
        self._theme = theme or dict(self._default_theme)
        self._backtrace = backtrace
        self._syntax_highlighter = SyntaxHighlighter(style)
        self._max_length = max_length
        self._encoding = encoding
        self._hidden_frames_filename = hidden_frames_filename
        self._prefix = prefix
        self._lib_dirs = self._get_lib_dirs()
        self._pipe_char = self._get_char("\u2502", "|")
        self._cap_char = self._get_char("\u2514", "->")
        self._catch_point_identifier = " <Loguru catch point here>"

    @staticmethod
    def _get_lib_dirs():
        pass

    @staticmethod
    def _indent(text, count, *, prefix="| "):
        pass

    def _get_char(self, char, default):
        pass

    def _is_file_mine(self, file):
        pass

    def _should_include_frame(self, frame):
        pass

    def _extract_frames(self, tb, is_first, *, limit=None, from_decorator=False):
        pass

    def _get_relevant_values(self, source, frame):
        pass

    def _format_relevant_values(self, relevant_values, colorize):
        pass

    def _format_value(self, v):
        pass

    def _format_locations(self, frames_lines, *, has_introduction):
        pass

    def _format_exception(
        self, value, tb, *, seen=None, is_first=False, from_decorator=False, group_nesting=0
    ):
        # Implemented from built-in traceback module:
        # https://github.com/python/cpython/blob/a5b76167/Lib/traceback.py#L468
        pass

    def _format_list(self, frames):

        pass

    def format_exception(self, type_, value, tb, *, from_decorator=False):
        pass
