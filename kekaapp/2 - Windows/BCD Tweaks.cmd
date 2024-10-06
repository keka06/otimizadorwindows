@echo off
echo Disable Dynamic Tick
echo Disable Synthetic Timers
@echo
bcdedit /set disabledynamictick yes
bcdedit /set useplatformtick yes
pause