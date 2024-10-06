@echo off
set "programa=C:\kekaapp\3 - Programas\DeviceCleanup.exe"

powershell -Command "Start-Process -FilePath '%programa%' -Verb RunAs"
