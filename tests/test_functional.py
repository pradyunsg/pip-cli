"""Tests that ensure that the cli does invoke the correct pip.
"""

import sys

from _pip_cli import main as cli_main

# Try to find the right place to patch the main function
try:
    from pip import _internal as pip_main_module
except ImportError:
    import pip as pip_main_module

from mock import Mock


def test_got_correct_pip_module():
    assert hasattr(pip_main_module, "main")


def test_pip_sees_the_command_line_arguments(monkeypatch):
    def check_arguments():
        import sys
        assert sys.argv[1:] == ["not-a-command"]

    my_mock = Mock()
    with monkeypatch.context() as m:
        # Modify sys.argv so that we can compare what we pass.
        m.setattr(sys, "argv", ["pip", "not-a-command"])
        # Patch the main function
        m.setattr(pip_main_module, "main", check_arguments)
        # Some versions of pip call sys.exit at some point, make it a no-op.
        m.setattr(sys, "exit", my_mock)

        # Call the entry-point; this should invoke pip.
        cli_main()
