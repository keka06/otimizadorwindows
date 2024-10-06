@echo off
echo Desativando servicos desnecessarios...
sc config "wsearch" start= disabled
sc stop wsearch
sc config "WerSvc" start= disabled
sc config "DiagTrack" start= disabled
sc config SysMain start= disabled
sc stop SysMain
echo Concluido!
pause
