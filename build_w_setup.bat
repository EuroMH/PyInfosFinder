@echo off
echo Cleaning up unnecessary files and directories...

:: Delete Python bytecode files
del /s /q *.pyc
del /s /q *.pyo
del /s /q __pycache__\*

:: Delete build, dist, and egg-info directories
rd /s /q build
rd /s /q dist
rd /s /q *.egg-info

:: Delete other temporary files if needed (e.g., .pytest_cache)
rd /s /q .pytest_cache

echo Cleanup complete.
pause
echo Building the module...
python setup.py sdist bdist_wheel
twine upload dist/*
