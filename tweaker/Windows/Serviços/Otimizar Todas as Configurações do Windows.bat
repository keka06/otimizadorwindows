Windows Registry Editor Version 5.00

;@(cls & %__APPDIR__%reg.exe import "%~f0" >nul 2>nul & goto :EOF)

; Aba de Contas ( Desativar sincronização )
[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync]
"SyncPolicy"=dword:00000005

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Personalization]
"Enabled"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\BrowserSettings]
"Enabled"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Credentials]
"Enabled"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Accessibility]
"Enabled"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Windows]
"Enabled"=dword:00000000

; Aba de Personalização ( Desativar Transparência )
[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize]
"EnableTransparency"=dword:00000000

; Guia de jogos E parte de configurações gráficas na guia Sistema
; Desativar barra de jogos e DVR de jogos
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowGameDVR]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\GameDVR] 
"AllowGameDVR"=dword:00000000

[HKEY_CURRENT_USER\System\GameConfigStore]
"GameDVR_Enabled"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR] 
"AppCaptureEnabled"=dword:00000000

; Ativar modo de jogo
[HKEY_CURRENT_USER\SOFTWARE\Microsoft\GameBar]
"AllowAutoGameMode"=dword:00000001
"AutoGameModeEnabled"=dword:00000001

; Ativar agendamento de GPU acelerado por hardware (Windows 10 2004 + NVIDIA 10 Series acima + AMD 5000 e acima)
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers]
"HwSchMode"=dword:00000002

; Desativar Refresh Rate
[HKEY_CURRENT_USER\SOFTWARE\Microsoft\DirectX\UserGpuPreferences]
"DirectXUserGlobalSettings"="VRROptimizeEnable=0;"

; Guia Facilidade de Acesso (Desativar Recursos de Facilidade de Acesso)
[HKEY_CURRENT_USER\Control Panel\Accessibility\MouseKeys]
"Flags"="0"

[HKEY_CURRENT_USER\Control Panel\Accessibility\StickyKeys]
"Flags"="0"

[HKEY_CURRENT_USER\Control Panel\Accessibility\Keyboard Response]
"Flags"="0"

[HKEY_CURRENT_USER\Control Panel\Accessibility\ToggleKeys]
"Flags"="0"

; Aba de Privacidade
; Guia geral
[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo]
"Enabled"=dword:00000000

[HKEY_CURRENT_USER\Control Panel\International\User Profile]
"HttpAcceptLanguageOptOut"=dword:00000001

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced]
"Start_TrackProgs"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager]
"SubscribedContent-338393Enabled"=dword:00000000
"SubscribedContent-353694Enabled"=dword:00000000
"SubscribedContent-353696Enabled"=dword:00000000

; Speech Tab
[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Speech_OneCore\Settings\OnlineSpeechPrivacy]
"HasAccepted"=dword:00000000

; Guia de personalização de tinta e digitação
[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Personalization\Settings]
"AcceptedPrivacyPolicy"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\InputPersonalization]
"RestrictImplicitInkCollection"=dword:00000001
"RestrictImplicitTextCollection"=dword:00000001

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\InputPersonalization\TrainedDataStore]
"HarvestContacts"=dword:00000000

; Guia de Diagnóstico e Feedback
[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Diagnostics\DiagTrack]
"ShowedToastAtLevel"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection]
"AllowTelemetry"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Privacy]
"TailoredExperiencesWithDiagnosticDataEnabled"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Diagnostics\DiagTrack\EventTranscriptKey]
"EnableEventTranscript"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Siuf\Rules]
"NumberOfSIUFInPeriod"=dword:00000000
"PeriodInNanoSeconds"=-

; Guia Histórico de atividades
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System]
"PublishUserActivities"=dword:00000000
"UploadUserActivities"=dword:00000000

; Aba Permissões do Aplicativo
; Disable Notifications - Location - App Diagnostics - Account Info Access
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userNotificationListener]
"Value"="Deny"

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location]
"Value"="Deny"

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appDiagnostics]
"Value"="Deny"

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userAccountInformation]
"Value"="Deny"

; Não permitir que aplicativos desnecessários sejam executados em segundo plano
[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications]
"GlobalUserDisabled"=dword:00000001

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search]
"BackgroundAppGlobalToggle"=dword:00000000

; Credits to Adamx                                                                