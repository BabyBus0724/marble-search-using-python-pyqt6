@echo off
setlocal

set NAME=run

cd %~dp0\..
pyinstaller.exe %NAME%.py --onefile --noconsole --clean
move dist\%NAME%.exe %~dp0\
rmdir /S /Q build dist
del %NAME%.spec
cd %~dp0
