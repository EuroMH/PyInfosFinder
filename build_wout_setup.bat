@echo off
echo Cleaning up unnecessary files and directories...

:: Delete Python bytecode files
del /s /q *.pyc
del /s /q *.pyo
del /s /q __pycache__\*

:: Delete build, dist, and egg-info directories
rd /s /q build
rd /s /q dist
rd /s /q PyInfosRetriver.egg-info

:: Delete other temporary files if needed (e.g., .pytest_cache)
rd /s /q .pytest_cache

echo Cleanup complete.

pause

cls

:: Set the PyPI token for Twine
set TWINE_PASSWORD=pypi-AgEIcHlwaS5vcmcCJDY5NjBiZjI2LWJkYWUtNGE4ZS1iMmFlLTcyM2QyNzRjZTEwYQACKlszLCI0NWUxMGZkYi0zYTdhLTQ5MWUtOGJjZS0
2NThkYWJkMTA5OWMiXQAABiD17_dL2lAUA6FqxcMFpu-b-dz7SNxdWyQtFsQOuv8K7g

:: Build the module
echo Building the module...
python -m build

:: Upload the distribution to PyPI using Twine
twine upload dist/*

:: Unset the PyPI token after upload for security
set TWINE_PASSWORD=

echo Upload complete.
pause
cls
echo installing the module.
cd dist
pip install pyinforetriever-0.1.0-py3-none-any.whl --force-reinstall
echo Succesfully installed the new veresion!
pause