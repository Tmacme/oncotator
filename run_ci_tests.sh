#!/bin/bash
# Have script stop if there is an error
set -e

# Make sure that a db-dir is specified, if not, set it to the default for the oncotator CI server at Broad.
if [ -z "$1" ]
  then
    echo "usage: run_ci_tests.sh <DB_DIR>";
    echo "    where <DB_DIR> is the location of your datasources ";
    exit 1
  else
    DB_DIR=${1}
fi


echo "This script must be run from the same directory as setup.py"

VENV=oncotator_nosetest_env_auto
rm -Rf $VENV
bash ./scripts/create_oncotator_venv.sh $VENV
source $VENV/bin/activate

# nosetests will return a non-zero error code if any unit test fails, so we do not want to stop this script
#   So we remove the error catching temporarily
python setup.py install

mkdir -p out
if [ -d "configs" ]
then
	echo "configs exists, doing nothing"
else
    ln -s test/configs configs
fi

if [ -d "testdata" ]
then
	echo "testdata exists, doing nothing"
else
    ln -s test/testdata testdata
fi

# Create a proper config file
sed -r "s:dbDir=MY_DB_DIR:dbDir=${DB_DIR}:g" configs/personal-test.config.template >configs/personal-test.config

set +e
nosetests --all-modules --exe --with-xunit -w test -v --processes=4 --process-timeout=480  --process-restartworker
set -e

echo "Deactivating and deleting test python virtual environment"
deactivate
rm -Rf $VENV