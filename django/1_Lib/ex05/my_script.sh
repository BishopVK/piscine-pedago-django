#!/bin/bash

# This file must be executed:
# > . my_script.sh
# or
# source my_script.sh

# Remove before create venv
rm -rf venv

# Create django_venv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Update pip
pip install --upgrade pip

# Install requirement.txt
pip install -r requirement.txt