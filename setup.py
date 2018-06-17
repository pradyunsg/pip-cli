import io
import os
import re
import sys

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with io.open(os.path.join(here, *parts), encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


entry_point_name = "_pip_cli:main"
script_names = [
    "pip",
    "pip%s" % sys.version_info[:1],
    "pip%s.%s" % sys.version_info[:2],
]

long_description = read("README.md")

setup(
    name="pip-cli",
    version=find_version("src", "_pip_cli.py"),
    license="MIT",
    url="https://github.com/pradyunsg/pip-cli",
    author="Pradyun Gedam",
    author_email='pradyunsg@gmail.com',

    description="Command line wrappers for pip.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["pip", "cli", "command-line"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],

    package_dir={"": "src"},
    py_modules=["_pip_cli"],

    entry_points={
        "console_scripts": [
            "{}={}".format(script, entry_point_name) for script in script_names
        ],
    },
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=["pip"]
)
