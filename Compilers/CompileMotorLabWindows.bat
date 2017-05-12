REM Place CompileMotorLab.bat and MotorLab.py and all associated files of
REM Motorlab in the same top directory of the pyinstaller-develop folder
REM Then you can run this script to compile to an .exe
cd ..
cd pyinstaller-develop
pyinstaller MotorLab.spec
pause