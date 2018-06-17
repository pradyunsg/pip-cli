import nox

# These were the 20 most used versions of pip on 17th May 2018
# https://github.com/pypa/packaging-problems/issues/58#issuecomment-389763639
PIP_VERSIONS = [
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


def do_a_test(session, pip_version):
    session.install("-r", "tools/tests-requirements.txt")
    session.install(".")

    if pip_version == "dev":
        session.install("https://github.com/pypa/pip/archive/master.zip")
    else:
        session.install("pip == {}".format(pip_version))

    session.run("pytest")


@nox.session
@nox.parametrize('pip_version', PIP_VERSIONS)
def test_27(session, pip_version):
    session.interpreter = "python2.7"
    do_a_test(session, pip_version)


@nox.session
@nox.parametrize('pip_version', PIP_VERSIONS)
def test_37(session, pip_version):
    session.interpreter = "python3.7"
    do_a_test(session, pip_version)


@nox.session
@nox.parametrize('pip_version', PIP_VERSIONS)
def test_36(session, pip_version):
    session.interpreter = "python3.6"
    do_a_test(session, pip_version)


@nox.session
@nox.parametrize('pip_version', PIP_VERSIONS)
def test_35(session, pip_version):
    session.interpreter = "python3.5"
    do_a_test(session, pip_version)


@nox.session
@nox.parametrize('pip_version', PIP_VERSIONS)
def test_34(session, pip_version):
    session.interpreter = "python3.4"
    do_a_test(session, pip_version)


@nox.session
@nox.parametrize('pip_version', PIP_VERSIONS)
def test_pypy(session, pip_version):
    session.interpreter = "pypy"
    do_a_test(session, pip_version)


@nox.session
@nox.parametrize('pip_version', PIP_VERSIONS)
def test_pypy3(session, pip_version):
    session.interpreter = "pypy3"
    do_a_test(session, pip_version)


@nox.session
def check(session):
    session.install("-r", "tools/check-requirements.txt")

    # linting
    session.run("flake8", "src", "tests", "tools")
    # packaging
    session.run("check-manifest")
    session.run("python", "setup.py", "check", "-m", "-s")

