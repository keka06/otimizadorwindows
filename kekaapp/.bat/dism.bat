@echo off
set "programa=C:\kekaapp\3 - Programas\Dism++\Dism++x64.exe"

powershell -Command "Start-Process -FilePath '%programa%' -Verb RunAs"
