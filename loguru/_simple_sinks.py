import inspect
import logging
import weakref

from ._asyncio_loop import get_running_loop, get_task_loop


class StreamSink:
    """A sink that writes log messages to a stream object.

    Parameters
    ----------
    stream
        A stream object that supports write operations.
    """

    def __init__(self, stream):
        self._stream = stream
        self._flushable = callable(getattr(stream, "flush", None))
        self._stoppable = callable(getattr(stream, "stop", None))
        self._completable = inspect.iscoroutinefunction(getattr(stream, "complete", None))

    def write(self, message):
        """Write a message to the stream.

        Parameters
        ----------
        message
            The message to write.
        """
        pass

    def stop(self):
        """Stop the stream if it supports the stop operation."""
        pass

    def tasks_to_complete(self):
        """Return list of tasks that need to be completed.

        Returns
        -------
        list
            List of tasks to complete.
        """
        pass


class StandardSink:
    """A sink that writes log messages using the standard logging module.

    Parameters
    ----------
    handler
        A logging handler instance.
    """

    def __init__(self, handler):
        self._handler = handler

    def write(self, message):
        """Write a message using the standard logging handler.

        Parameters
        ----------
        message
            The message to write.
        """
        pass

    def stop(self):
        """Close the logging handler."""
        pass

    def tasks_to_complete(self):
        """Return list of tasks that need to be completed.

        Returns
        -------
        list
            Empty list as standard sink has no async tasks.
        """
        pass


class AsyncSink:
    """A sink that handles asynchronous logging operations.

    Parameters
    ----------
    function
        The async function to execute.
    loop
        The event loop to use.
    error_interceptor
        An interceptor for handling errors.
    """

    def __init__(self, function, loop, error_interceptor):
        self._function = function
        self._loop = loop
        self._error_interceptor = error_interceptor
        self._tasks = weakref.WeakSet()

    def write(self, message):
        """Asynchronously write a message.

        Parameters
        ----------
        message
            The message to write.
        """
        pass

    def stop(self):
        """Cancel all pending tasks."""
        pass

    def tasks_to_complete(self):
        """Return list of tasks that need to be completed.

        Returns
        -------
        list
            List of tasks to complete.
        """
        pass

    async def _complete_task(self, task):
        """Complete a single task.

        Parameters
        ----------
        task
            The task to complete.
        """
        pass

    def __getstate__(self):
        state = self.__dict__.copy()
        state["_tasks"] = None
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self._tasks = weakref.WeakSet()


class CallableSink:
    """A sink that executes a callable function for each log message.

    Parameters
    ----------
    function
        The function to call for each message.
    """

    def __init__(self, function):
        self._function = function

    def write(self, message):
        """Write a message by calling the function.

        Parameters
        ----------
        message
            The message to pass to the function.
        """
        pass

    def stop(self):
        """Stop the sink (no-op for callable sink)."""
        pass

    def tasks_to_complete(self):
        """Return list of tasks that need to be completed.

        Returns
        -------
        list
            Empty list as callable sink has no tasks.
        """
        pass
