@echo off
set path=%path%;C:\Python27\
set PYTHONPATH=C:\Python27;C:\Python27\Lib
@echo on

cd ..\..
C:\Python27\python generator.pyc "14103_SBC" UTF-8
@REM C:\Python27\python generator.pyc "EasterDate" UTF-8

xcopy .\projects\14103_SBC\src .\projects\14103_SBC\release

@echo Fertig.

@pause