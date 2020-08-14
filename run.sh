#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python run.py $1 $2