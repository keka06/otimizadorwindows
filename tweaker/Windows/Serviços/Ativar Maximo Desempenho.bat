@echo off
cls
echo.
echo Aperte a tecla "1" para habilitar o plano de energia e logo em seguida "enter"
echo.
echo.
echo [1] HABILITAR

set /p opcao=Digite a escolha desejada:

if "%opcao%" == "1" goto op1

:op1
powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
goto fim

:fim
echo.
echo Novo plano de energia habilitado com sucesso!
echo.
echo Pressione qualquer tecla para sair...
pause > nul