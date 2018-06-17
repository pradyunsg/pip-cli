"""Command Line Wrappers for pip
"""

__version__ = "0.1.0.dev0"


def main():
    # pip-cli does not modify any state of the running interpreter in any
    # manner that would affect pip. Using pip in-process works out fine here
    # since this module does not care about how the behavior of this system is.
    #
    # Using pip in-process as a part of a larger program is *not* supported. A
    # related discussion as well as a few supported ways of using pip is at
    # https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program
    import runpy

    runpy.run_module(
        "pip",
        init_globals={"_PIP_CLI_VERSION": __version__},
        run_name="__main__",
    )
