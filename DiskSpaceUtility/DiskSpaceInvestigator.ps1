# ============================================
# Disk Space Investigator for Windows
# Run: Right-click > Run with PowerShell
# Or:  powershell -ExecutionPolicy Bypass -File DiskSpaceInvestigator.ps1
# ============================================

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   DISK SPACE INVESTIGATOR" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# --- Current Drive Status ---
$drive = Get-PSDrive C
Write-Host "[DRIVE STATUS]" -ForegroundColor Yellow
Write-Host "  Total:  $([math]::Round(($drive.Used + $drive.Free)/1GB,2)) GB"
Write-Host "  Used:   $([math]::Round($drive.Used/1GB,2)) GB"
Write-Host "  Free:   $([math]::Round($drive.Free/1GB,2)) GB"
Write-Host ""

# --- Helper function ---
function Get-FolderSizeGB($path) {
    if (Test-Path $path) {
        $size = (Get-ChildItem $path -Recurse -ErrorAction SilentlyContinue -File | Measure-Object -Property Length -Sum).Sum
        return [math]::Round($size/1GB,2)
    }
    return 0
}

# --- Temp Folders ---
Write-Host "[TEMP FOLDERS]" -ForegroundColor Yellow
$userTemp = Get-FolderSizeGB $env:TEMP
$winTemp = Get-FolderSizeGB "C:\Windows\Temp"
Write-Host "  User Temp ($env:TEMP): $userTemp GB"
Write-Host "  Windows Temp: $winTemp GB"
Write-Host ""

# --- Top .node cache files in Temp ---
$nodeFiles = Get-ChildItem $env:TEMP -Filter "*.node" -ErrorAction SilentlyContinue
$nodeSize = ($nodeFiles | Measure-Object -Property Length -Sum).Sum
if ($nodeSize -gt 0) {
    Write-Host "  >> V8 .node cache files in Temp: $($nodeFiles.Count) files, $([math]::Round($nodeSize/1GB,2)) GB" -ForegroundColor Red
}
Write-Host ""

# --- VHDX Virtual Disks (Docker, WSL) ---
Write-Host "[VIRTUAL DISKS (VHDX)]" -ForegroundColor Yellow
Get-ChildItem "C:\Users" -Recurse -Include "*.vhdx" -ErrorAction SilentlyContinue -Force | ForEach-Object {
    Write-Host "  $([math]::Round($_.Length/1GB,2)) GB  $($_.FullName)  (Modified: $($_.LastWriteTime))"
}
Write-Host ""

# --- AppData Breakdown ---
Write-Host "[APPDATA - LOCAL (folders > 100 MB)]" -ForegroundColor Yellow
Get-ChildItem "$env:LOCALAPPDATA" -Directory -ErrorAction SilentlyContinue | ForEach-Object {
    $size = (Get-ChildItem $_.FullName -Recurse -ErrorAction SilentlyContinue -File | Measure-Object -Property Length -Sum).Sum
    if ($size -gt 100MB) {
        [PSCustomObject]@{ Folder = $_.Name; SizeGB = [math]::Round($size/1GB,2) }
    }
} | Sort-Object SizeGB -Descending | ForEach-Object {
    Write-Host "  $($_.SizeGB) GB`t$($_.Folder)"
}
Write-Host ""

Write-Host "[APPDATA - ROAMING (folders > 100 MB)]" -ForegroundColor Yellow
Get-ChildItem "$env:APPDATA" -Directory -ErrorAction SilentlyContinue | ForEach-Object {
    $size = (Get-ChildItem $_.FullName -Recurse -ErrorAction SilentlyContinue -File | Measure-Object -Property Length -Sum).Sum
    if ($size -gt 100MB) {
        [PSCustomObject]@{ Folder = $_.Name; SizeGB = [math]::Round($size/1GB,2) }
    }
} | Sort-Object SizeGB -Descending | ForEach-Object {
    Write-Host "  $($_.SizeGB) GB`t$($_.Folder)"
}
Write-Host ""

# --- Package Manager Caches ---
Write-Host "[PACKAGE MANAGER CACHES]" -ForegroundColor Yellow
$caches = @(
    @{ Name = "Yarn";       Path = "$env:LOCALAPPDATA\Yarn" },
    @{ Name = "npm-cache";  Path = "$env:LOCALAPPDATA\npm-cache" },
    @{ Name = "pnpm-cache"; Path = "$env:LOCALAPPDATA\pnpm-cache" },
    @{ Name = "pnpm-store"; Path = "$env:LOCALAPPDATA\pnpm" },
    @{ Name = "uv (Local)"; Path = "$env:LOCALAPPDATA\uv" },
    @{ Name = "uv (Roam)";  Path = "$env:APPDATA\uv" },
    @{ Name = "go-build";   Path = "$env:LOCALAPPDATA\go-build" },
    @{ Name = "pip";        Path = "$env:LOCALAPPDATA\pip" }
)
foreach ($c in $caches) {
    $size = Get-FolderSizeGB $c.Path
    if ($size -gt 0) {
        Write-Host "  $size GB`t$($c.Name)"
    }
}
Write-Host ""

# --- User Profile Folders ---
Write-Host "[USER PROFILE FOLDERS]" -ForegroundColor Yellow
$userDirs = @('Desktop','Documents','Downloads','Videos','Music','Pictures')
foreach ($dir in $userDirs) {
    $path = Join-Path $env:USERPROFILE $dir
    $size = Get-FolderSizeGB $path
    if ($size -gt 0.01) {
        Write-Host "  $size GB`t$dir"
    }
}
Write-Host ""

# --- Recycle Bin ---
Write-Host "[RECYCLE BIN]" -ForegroundColor Yellow
try {
    $shell = New-Object -ComObject Shell.Application
    $rb = $shell.Namespace(0xA)
    Write-Host "  Items: $($rb.Items().Count)"
} catch {
    Write-Host "  Could not query Recycle Bin"
}
Write-Host ""

# --- Windows Update Cache ---
Write-Host "[WINDOWS UPDATE CACHE]" -ForegroundColor Yellow
$wuSize = Get-FolderSizeGB "C:\Windows\SoftwareDistribution"
Write-Host "  SoftwareDistribution: $wuSize GB"
Write-Host ""

# --- Top-level C:\ folders ---
Write-Host "[TOP-LEVEL C:\ FOLDERS]" -ForegroundColor Yellow
Get-ChildItem "C:\" -Directory -ErrorAction SilentlyContinue | ForEach-Object {
    $size = (Get-ChildItem $_.FullName -Recurse -ErrorAction SilentlyContinue -File | Measure-Object -Property Length -Sum).Sum
    if ($size -gt 500MB) {
        [PSCustomObject]@{ Folder = $_.Name; SizeGB = [math]::Round($size/1GB,2) }
    }
} | Sort-Object SizeGB -Descending | ForEach-Object {
    Write-Host "  $($_.SizeGB) GB`t$($_.Folder)"
}
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   INVESTIGATION COMPLETE" -ForegroundColor Cyan
Write-Host "   Run DiskSpaceCleaner.ps1 to clean up" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Read-Host "Press Enter to exit"
