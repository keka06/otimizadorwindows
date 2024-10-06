@echo off
set "programa=C:\kekaapp\3 - Programas\Temp Cleaner.exe"

powershell -Command "Start-Process -FilePath '%programa%' -Verb RunAs"
