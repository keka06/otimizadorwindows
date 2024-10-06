Windows Registry Editor Version 5.00

;@(cls & %__APPDIR__%reg.exe import "%~f0" >nul 2>nul & goto :EOF)

; Disable Connected User Experiences and Telemetry
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\DiagTrack]
"Start"=dword:00000004

; Disable dmwappushservice
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\dmwappushservice]
"Start"=dword:00000004

; Disable Diagnostic Execution Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\diagsvc]
"Start"=dword:00000004

; Disable Diagnostic Policy Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\DPS]
"Start"=dword:00000004

; Disable Microsoft (R) Diagnostics Hub Standard Collector Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\diagnosticshub.standardcollector.service]
"Start"=dword:00000004

; Disable Diagnostic Service Host
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdiServiceHost]
"Start"=dword:00000004

; Disable Diagnostic System Host
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdiSystemHost]
"Start"=dword:00000004

;Disable Windows Biometric Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc]
"Start"=dword:00000004

;Disable Windows Font Cache Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\FontCache]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\FontCache3.0.0.0]
"Start"=dword:00000004

;Disable Graphics performance monitor service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\GraphicsPerfSvc]
"Start"=dword:00000004

;Disable Windows Image Acquisition (WIA)
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\stisvc]
"Start"=dword:00000004

;Disable Windows Error Reporting Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WerSvc]
"Start"=dword:00000004

;Disable Program Compatibility Assistant Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PcaSvc]
"Start"=dword:00000004

;Disable Windows Event Collector
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Wecsvc]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MapsBroker]
"Start"=dword:00000004

;Disable Bluetooth Audio Gateway Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\BTAGService]
"Start"=dword:00000004

;Disable Bluetooth Support Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\bthserv]
"Start"=dword:00000004

;Disable Print Spooler
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Spooler]
"Start"=dword:00000004

;Disable Printer Extensions and Notifications
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PrintNotify]
"Start"=dword:00000004

;Disable Xbox Live Game Save
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\XblGameSave]
"Start"=dword:00000004

;Disable Xbox Live Networking Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\XboxNetApiSvc]
"Start"=dword:00000004

;Disable Xbox Accessory Management Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\XboxGipSvc]
"Start"=dword:00000004

;Disable Xbox Live Auth Manager
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\XblAuthManager]
"Start"=dword:00000004