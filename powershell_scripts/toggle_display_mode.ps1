Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class DisplayModeInfo
{
    [DllImport("user32.dll")]
    public static extern int GetSystemMetrics(int nIndex);
}
"@

$SM_CMONITORS = 80
$displaySettings = [DisplayModeInfo]::GetSystemMetrics($SM_CMONITORS)
$displayMode = ""
$displayNumber = $displaySettings

if ($displayNumber -eq 1) {
    $displayMode = "Dublicated Display"
    DisplaySwitch.exe /extend
}
elseif ($displayNumber -eq 2) {
    $displayMode = "Extended Displays"
    DisplaySwitch.exe /clone
}
else {
    $displayMode = "Unknown"
    Write-Host "Current Display Mode: $displayMode ($displayNumber)"
    Pause
}
