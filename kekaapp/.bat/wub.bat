@echo off
set "programa=C:\kekaapp\3 - Programas\Wub\Wub.exe"

powershell -Command "Start-Process -FilePath '%programa%' -Verb RunAs"
