"""This package defines exception base classes."""

from enum import Enum


class ErrorCode(Enum):
    """EDB Exception Types."""

    UNKNOWN = "Unknown exception: {}."
    UNAVAILABLE = "EDB Server is not accessible. Please make sure it's up and running."

    NO_SESSIONS = "No active session detected."

    STARTUP_UNEXPECTED = "An unexpected error occurred when starting the local server: {}."
    STARTUP_TIMEOUT = "There can be only one session active at a time."
    STARTUP_MULTI_SESSIONS = "There can be only one session active at a time."
    STARTUP_NO_EXECUTABLE = (
        "Could not find necessary executables. Make sure Ansys EM root directory is correct."
    )
    STARTUP_FAILURE_LICENSE = "Could not start local server: No valid license detected."
    STARTUP_FAILURE_EDB = "Could not start local server: Failed to initialize EDB."
    STARTUP_FAILURE = "Could not start local server due to unknown reason."

    INVALID_ARGUMENT = "{}"


def _message(code, *args):
    template = code.value
    return template.format(*args)


class EDBSessionException(Exception):
    """Base class for exceptions related to EDB sessions."""

    def __init__(self, code, *args):
        """Initialize EDBSessionException."""
        super().__init__(_message(code, *args))
        self._code = code


class InvalidArgumentException(EDBSessionException):
    """Exception when a request fails due to invalid argument."""

    def __init__(self, response):
        """Initialize InvalidArgumentException."""
        super().__init__(ErrorCode.INVALID_ARGUMENT, response.details())
        self._response = response
