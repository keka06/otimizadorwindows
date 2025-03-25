Windows Registry Editor Version 5.00

;@(cls & %__APPDIR__%reg.exe import "%~f0" >nul 2>nul & goto :EOF)

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\GpuEnergyDrv]
"Start"=dword:00000004

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Avalon.Graphics]
"MaxMultisampleType"=dword:00000000

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDriver]
"HwSchMode"=dword:00000002