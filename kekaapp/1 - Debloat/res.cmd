@echo off
setlocal

:: Define o nome do ponto de restauração
set "restoreName=keka"

:: Cria o ponto de restauração
wmic.exe /namespace:\\root\default path SystemRestore call CreateRestorePoint "%restoreName%", 100, 7

echo Ponto de restauração "%restoreName%" criado com sucesso.
pause
endlocal
