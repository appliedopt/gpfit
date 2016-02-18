#!/bin/bash

# This means you can run the script anywhere in the repo, but not outside
WORKSPACE=$(git rev-parse --show-toplevel)

# Calling pylint directly will not work correcly in a virtualenv if pylint is not installed in the venv
# Using python with the pylint script will always work properly in a virtualenv
PYLINT=`which pylint`

python $PYLINT --rcfile=$WORKSPACE/.pylintrc $@ $WORKSPACE/gpfit/

python $PYLINT --rcfile=$WORKSPACE/.pylintrc --disable=invalid-name,too-many-locals $@ $WORKSPACE/docs/source/examples/*.py
