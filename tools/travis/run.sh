set -e

if [[ ${SESSION} == "" ]]; then
  if [[ ${TRAVIS_PYTHON_VERSION} == pypy* ]]; then
      export SESSION="test_${TRAVIS_PYTHON_VERSION}"
  else
      # We use the syntax ${string:index:length} to make 2.7 -> py27
      _major=${TRAVIS_PYTHON_VERSION:0:1}
      _minor=${TRAVIS_PYTHON_VERSION:2:1}
      export SESSION="test_${_major}${_minor}"
  fi
fi

nox -s ${SESSION}
