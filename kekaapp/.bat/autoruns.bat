@echo off
set "programa=C:\kekaapp\3 - Programas\AutoRuns.exe"

powershell -Command "Start-Process -FilePath '%programa%' -Verb RunAs"
