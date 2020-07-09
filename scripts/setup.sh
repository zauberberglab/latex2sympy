#!/bin/sh

# Get relative path of the root directory of the project
rdir=`git rev-parse --git-dir`
rel_path="$(dirname "$rdir")"
# Change to that path and run the file
cd $rel_path

echo "creating venv..."
if test -d .env
then echo "venv exists"
else python -m venv .env && echo "venv created"
fi

echo ''
# Activate virtual environment
echo "activating venv..."
if test -f .env/bin/activate
then source .env/bin/activate && echo "venv activate (bin)"
elif test -f .env/Scripts/activate
then source .env/Scripts/activate && echo "venv activated (Scripts)"
else exit 1
fi

echo ''
echo "installing requirements..."
if pip install -r dev-requirements.txt
then echo "requirements installed"
else exit 1
fi

echo ''
echo "compiling parser..."
java -jar antlr-4.7.2-complete.jar PS.g4 -o gen
echo "parser compiled"

exit 0
