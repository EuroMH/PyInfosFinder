@echo off
echo Cleaning up unnecessary files and directories...

del /s /q *.pyc
del /s /q *.pyo
del /s /q __pycache__\*

rd /s /q build
rd /s /q dist
rd /s /q PyInfosRetriver.egg-info

rd /s /q .pytest_cache

echo Cleanup complete.
cls

echo Building the module...
python -m build

twine upload dist/*

echo Upload complete.
cls
echo installing the module.
cd dist
pip install pyinforetriever-0.1.0-py3-none-any.whl --force-reinstall
echo Succesfully installed the new veresion!