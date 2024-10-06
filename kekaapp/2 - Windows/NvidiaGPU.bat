Windows Registry Editor Version 5.00
echo Batch File By zJu4nn

;@(cls & %__APPDIR__%reg.exe import "%~f0" >nul 2>nul & goto :EOF)		

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers]
"RmGpsPsEnablePerCpuCoreDpc"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power]
"RmGpsPsEnablePerCpuCoreDpc"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\nvlddmkm]
"RmGpsPsEnablePerCpuCoreDpc"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\nvlddmkm\NVAPI]
"RmGpsPsEnablePerCpuCoreDpc"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\nvlddmkm\Global\NVTweak]
"RmGpsPsEnablePerCpuCoreDpc"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\GpuEnergyDrv]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\nvlddmkm\FTS]
"EnableRID61684"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\nvlddmkm\Global\NVTweak]
"DisplayPowerSaving"=dword:00000000

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\nvlddmkm]
"DisablePreemption"=dword:00000001
"DisableCudaContextPreemption"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler]
"EnablePreemption"=dword:00000000

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\nvlddmkm]
"DisableWriteCombining"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\nvlddmkm\FTS]
"EnableRID61684"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\nvlddmkm]
"DisableWriteCombining"=dword:00000001