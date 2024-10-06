@echo off
set "programa=C:\kekaapp\3 - Programas\Ultimate Windows Tweaker 4.8.exe"

powershell -Command "Start-Process -FilePath '%programa%' -Verb RunAs"
