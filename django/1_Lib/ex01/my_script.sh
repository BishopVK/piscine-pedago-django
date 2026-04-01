#!/bin/bash

# Verify pip version
echo "pip version:"
pip --version

# Remove before path installation
rm -rf local_lib

echo "Installing 'path'..."

# Install path in local_lib, saving stdout and stderr log into a file
pip install --target=local_lib git+https://github.com/jaraco/path.git > install.log 2>&1
INSTALL_STATUS=$?

# Check if install was correctly
if [ $INSTALL_STATUS -eq 0 ]; then
    echo "'path' was installed correctly"
    echo "Executing my_program.py..."
    PYTHONPATH="$(pwd)/local_lib" python3 my_program.py
else
    echo "The installation of 'path' failed"
    exit 1
fi