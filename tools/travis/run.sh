set -e

if [[ ${SESSION} != "" ]]; then
  nox -s ${SESSION}
else
  # Don't keep the 3.7"-dev" suffix
  if [[ $TRAVIS_PYTHON_VERSION == "3.7-dev" ]]; then
    TRAVIS_PYTHON_VERSION=3.7
  fi

  tmp_file=/tmp/nox-cli.txt

  # Dump all the shell commands to a file
  nox -l | grep "python_version='${TRAVIS_PYTHON_VERSION}'" | cut -c 3- | while read line; do
    echo "-s" >> $tmp_file
    echo "${line}" >> $tmp_file
  done

  if [ ! -f $tmp_file ]; then
    echo -n "Failed to find any sessions for ${TRAVIS_PYTHON_VERSION} in"
    nox -l
    exit 1
  fi

  # Pass all the nox sessions to nox.
  OLD_IFS=$IFS
  IFS=$'\n'
  nox $(cat $tmp_file)
  IFS=$OLD_IFS

  # Remove that temporary file
  rm $tmp_file
fi
