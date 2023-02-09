#!/bin/sh

python3 -m virtualenv django_venv

. django_venv/bin/activate

pip3 install -r requirement.txt