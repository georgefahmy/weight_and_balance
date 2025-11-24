#!/bin/bash

INVENV=$(/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 -c 'import sys; print( True if "virtual" in sys.prefix else False)')
VERSION=v$(/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 setup.py --version)

if [ $INVENV == "True" ]; then
    echo "Please deactivate the virtual environment and run again"
    exit 0
else
    rm -rf build dist
    /Library/Frameworks/Python.framework/Versions/3.12/bin/pip3 install -r requirements.txt
    /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 setup.py py2app -A
    cd dist
    ln -s /Applications/
    echo "Creating Installation Image"
    hdiutil create -srcfolder . -volname "WeightAndBalance" WeightAndBalance.dmg
    rm -rf "WeightAndBalance.app"
    rm ./Applications
    cd ..
    echo "Creating release $VERSION and uploading app to github"
    gh release create $VERSION ./dist/*.dmg -t "WeightAndBalance $VERSION"  -F changelog.md
fi