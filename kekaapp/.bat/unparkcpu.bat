@echo off
set "programa=C:\kekaapp\3 - Programas\UnparkCpu.exe"

powershell -Command "Start-Process -FilePath '%programa%' -Verb RunAs"
