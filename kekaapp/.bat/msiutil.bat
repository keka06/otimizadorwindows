@echo off
set "programa=C:\kekaapp\3 - Programas\MSI Util V3.exe"

powershell -Command "Start-Process -FilePath '%programa%' -Verb RunAs"
