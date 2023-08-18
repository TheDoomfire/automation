# Prompt for elevation if not already running as administrators
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
   $arguments = "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`""
   Start-Process -FilePath "powershell.exe" -Verb RunAs -ArgumentList $arguments
   Exit
   }   

$newSpeed = 20

set-strictMode -version latest

$winApi = add-type -name user32 -namespace tq84 -passThru -memberDefinition '
   [DllImport("user32.dll")]
    public static extern bool SystemParametersInfo(
       uint uiAction,
       uint uiParam ,
       uint pvParam ,
       uint fWinIni
    );
'

$SPI_SETMOUSESPEED = 0x0071

"MouseSensitivity before WinAPI call:  $((get-itemProperty 'hkcu:\Control Panel\Mouse').MouseSensitivity)"

$null = $winApi::SystemParametersInfo($SPI_SETMOUSESPEED, 0, $newSpeed, 0)

#
#    Calling SystemParametersInfo() does not permanently store the modification
#    of the mouse speed. It needs to be changed in the registry as well
#
"MouseSensitivity after WinAPI call:  $((get-itemProperty 'hkcu:\Control Panel\Mouse').MouseSensitivity)"

set-itemProperty 'hkcu:\Control Panel\Mouse' -name MouseSensitivity -value $newSpeed