#!/bin/sh

pip --version

pip install --force-reinstall --target=./local_lib git+https://github.com/jaraco/path.git > install.log 2>&1