"""Command Line Wrapper for pip
"""

import os
import sys
import textwrap
import warnings
from distutils.spawn import find_executable

__version__ = "0.1.0.dev0"


def format_warning(format_string, **kwargs):
    """A shorthand to make it easier to write error messages.
    """
    return textwrap.dedent(format_string.strip().format(**kwargs))


def running_under_virtualenv():
    """Is this running inside a virtualenv?
    """
    if hasattr(sys, "real_prefix"):
        return True
    elif sys.prefix != getattr(sys, "base_prefix", sys.prefix):
        return True

    return False


def warn_about_mismatching_python(executable, path):
    # Don't perform this check when it's running in a virtualenv. They're
    # assumed to be sane environments.
    if running_under_virtualenv():
        return

    # Look for the executable
    expected_name = os.path.basename(executable)
    first_python_found = find_executable(expected_name, path=path)

    if first_python_found is None:
        return format_warning(
            """
            No executable found for {executable!r} on PATH. See <todo-docs-link> for
            troubleshooting help.
            """,
            executable=executable,
        )
    else:
        found = os.path.normpath(first_python_found)
        expected = os.path.normpath(executable)
        if found != expected:
            return format_warning(
                """
                There is a mismatch between {executable!r} on PATH and the
                executable used to invoke pip.
                """,
                executable=executable,
            )


def main():
    # pip-cli warns the user if there's a mismatch between 'python' on PATH and
    # sys.executable.
    warn_about_mismatching_python(sys.executable, os.environ["PATH"])

    # pip-cli does not modify any state of the running interpreter in any manner
    # that would affect pip _and_ this module does not do anything after pip
    # returns/exits.
    #
    # Using pip in-process as a part of a larger program is *not* supported. A
    # related discussion on the supported ways of using pip can be found at
    # https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program.
    import runpy

    runpy.run_module(
        "pip",
        init_globals={"_PIP_CLI_VERSION": __version__},
        run_name="__main__",
    )
