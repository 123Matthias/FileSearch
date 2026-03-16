;TODO Check Versioning
#define MyAppName "FileSearch"
#define MyAppVersion "v0.0.0-alpha"
#define MyAppPublisher "123Matthias GitHub"
#define MyAppURL "https://github.com/123Matthias/FileSearch"
#define MyAppExeName MyAppName + ".exe"
#define MyAppExeVersion MyAppName + " " + MyAppVersion + ".exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{E957AF66-DA9A-46B3-BFD0-52DE4FC9A718}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeVersion}
; "ArchitecturesAllowed=x64compatible" specifies that Setup cannot run
; on anything but x64 and Windows 11 on Arm.
ArchitecturesAllowed=x64compatible
; "ArchitecturesInstallIn64BitMode=x64compatible" requests that the
; install be done in "64-bit mode" on x64 or Windows 11 on Arm,
; meaning it should use the native 64-bit Program Files directory and
; the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64compatible
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only).
;PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=C:\Users\leite\Desktop\FileSearchApp
OutputBaseFilename=FileSearch_{#MyAppVersion}_Setup
SetupIconFile=C:\git\OSWalk\assets\img\logo.ico
SolidCompression=yes
WizardStyle=modern windows11

; ===== NEU: Diese Zeilen für Update-Fragen =====
UsePreviousAppDir=yes
UsePreviousGroup=yes
UsePreviousSetupType=yes
UsePreviousLanguage=yes
ShowLanguageDialog=no
AppMutex=FileSearchMutex
CreateUninstallRegKey=yes
Uninstallable=yes
; ===== ENDE NEU =====

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked


[Files]
; 1. Die EXE aus PyInstaller (heißt FileSearch.exe) wird mit Version umbenannt
Source: "C:\git\OSWalk\dist\FileSearch\{#MyAppExeName}"; DestDir: "{app}"; DestName: "{#MyAppExeVersion}"; Flags: ignoreversion

; 2. ALLES aus _internal nach {app}\_internal (wie PyInstaller es baut!)
Source: "C:\git\OSWalk\dist\FileSearch\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs createallsubdirs

; 3. ZUSÄTZLICH: DLLs auch ins Hauptverzeichnis (damit EXE sie findet)
Source: "C:\git\OSWalk\dist\FileSearch\_internal\*.dll"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeVersion}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeVersion}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeVersion}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent