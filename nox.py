import nox

@nox.session
@nox.parametrize('python_version', [
        '2.7',
        '3.7',
        '3.6',
        '3.5',
        '3.4',
        'pypy',
        'pypy3',
    ]
)
@nox.parametrize(
    'pip_version', [
        # These were the 20 most used versions of pip on 17th May 2018
        # https://github.com/pypa/packaging-problems/issues/58#issuecomment-389763639
        "1.4.1",
        "1.5.4",
        "1.5.5",
        "1.5.6",
        "6.0.8",
        "6.1.1",
        "7.0.1",
        "7.1.0",
        "7.1.2",
        "8.0.2",
        "8.0.3",
        "8.1.1",
        "8.1.2",
        "9.0.0",
        "9.0.1",
        "9.0.2",
        "9.0.3",
        "10.0.0",
        "10.0.1",
        "dev",
    ]
)
def test(session, python_version, pip_version):
    # Set the interpreter
    if python_version.startswith("pypy"):
        session.interpreter = python_version
    else:
        session.interpreter = "python" + python_version

    session.install("-r", "tools/tests-requirements.txt")
    session.install(".")

    if pip_version == "dev":
        session.install("https://github.com/pypa/pip/archive/master.zip")
    else:
        session.install("pip == {}".format(pip_version))

    session.run("pytest")


@nox.session
def check(session):
    session.install("-r", "tools/check-requirements.txt")

    # linting
    session.run("flake8", "src", "tests", "tools")
    # packaging
    session.run("check-manifest")
    session.run("python", "setup.py", "check", "-m", "-s")

