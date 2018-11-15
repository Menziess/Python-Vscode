#!/bin/bash

if [ ! -d "$venv" ]; then
  virtualenv venv
fi

source venv/bin/activate
export FLASK_APP="src/app.py"
export FLASK_ENV="development"
pip install -r requirements.txt
python setup.py develop

