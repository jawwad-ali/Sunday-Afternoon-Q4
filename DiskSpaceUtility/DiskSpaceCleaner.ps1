# ============================================
# Disk Space Cleaner for Windows
# Run as Administrator for full cleanup
# Right-click > Run with PowerShell
# Or:  powershell -ExecutionPolicy Bypass -File DiskSpaceCleaner.ps1
# ============================================

function Get-FolderSizeGB($path) {
    if (Test-Path $path) {
        $size = (Get-ChildItem $path -Recurse -ErrorAction SilentlyContinue -File | Measure-Object -Property Length -Sum).Sum
        return [math]::Round($size/1GB,2)
    }
    return 0
}

function Show-Menu {
    $drive = Get-PSDrive C
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "   DISK SPACE CLEANER" -ForegroundColor Cyan
    Write-Host "   Free: $([math]::Round($drive.Free/1GB,2)) GB" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  [1] Clean User Temp Folder        ($(Get-FolderSizeGB $env:TEMP) GB)"
    Write-Host "  [2] Clean Yarn Cache              ($(Get-FolderSizeGB "$env:LOCALAPPDATA\Yarn") GB)"
    Write-Host "  [3] Clean npm Cache               ($(Get-FolderSizeGB "$env:LOCALAPPDATA\npm-cache") GB)"
    Write-Host "  [4] Clean pnpm Cache              ($([math]::Round((Get-FolderSizeGB "$env:LOCALAPPDATA\pnpm-cache") + (Get-FolderSizeGB "$env:LOCALAPPDATA\pnpm"),2)) GB)"
    Write-Host "  [5] Clean uv Cache (Python)       ($([math]::Round((Get-FolderSizeGB "$env:LOCALAPPDATA\uv") + (Get-FolderSizeGB "$env:APPDATA\uv"),2)) GB)"
    Write-Host "  [6] Clean Go Build Cache          ($(Get-FolderSizeGB "$env:LOCALAPPDATA\go-build") GB)"
    Write-Host "  [7] Compact Docker VHDX           (requires Admin + Docker stopped)"
    Write-Host "  [8] Empty Recycle Bin"
    Write-Host "  [A] Run ALL of the above"
    Write-Host "  [Q] Quit"
    Write-Host ""
}

function Clean-TempFolder {
    Write-Host ""
    Write-Host "--- Cleaning User Temp Folder ---" -ForegroundColor Yellow
    $before = (Get-PSDrive C).Free
    $deleted = 0; $skipped = 0
    Get-ChildItem $env:TEMP -ErrorAction SilentlyContinue | ForEach-Object {
        try {
            Remove-Item $_.FullName -Recurse -Force -ErrorAction Stop
            $deleted++
        } catch {
            $skipped++
        }
    }
    $after = (Get-PSDrive C).Free
    Write-Host "  Deleted: $deleted items | Skipped (in use): $skipped" -ForegroundColor Green
    Write-Host "  Reclaimed: $([math]::Round(($after - $before)/1GB,2)) GB" -ForegroundColor Green
}

function Clean-YarnCache {
    Write-Host ""
    Write-Host "--- Cleaning Yarn Cache ---" -ForegroundColor Yellow
    $before = (Get-PSDrive C).Free
    $yarnCmd = Get-Command yarn -ErrorAction SilentlyContinue
    if ($yarnCmd) {
        yarn cache clean 2>&1 | Out-Null
    } else {
        Remove-Item "$env:LOCALAPPDATA\Yarn\Cache" -Recurse -Force -ErrorAction SilentlyContinue
    }
    $after = (Get-PSDrive C).Free
    Write-Host "  Reclaimed: $([math]::Round(($after - $before)/1GB,2)) GB" -ForegroundColor Green
}

function Clean-NpmCache {
    Write-Host ""
    Write-Host "--- Cleaning npm Cache ---" -ForegroundColor Yellow
    $before = (Get-PSDrive C).Free
    $npmCmd = Get-Command npm -ErrorAction SilentlyContinue
    if ($npmCmd) {
        npm cache clean --force 2>&1 | Out-Null
    }
    # Also clean _npx and other leftover dirs
    $extraDirs = @('_npx', '_libvips', '_prebuilds')
    foreach ($d in $extraDirs) {
        $path = "$env:LOCALAPPDATA\npm-cache\$d"
        if (Test-Path $path) {
            Remove-Item $path -Recurse -Force -ErrorAction SilentlyContinue
        }
    }
    $after = (Get-PSDrive C).Free
    Write-Host "  Reclaimed: $([math]::Round(($after - $before)/1GB,2)) GB" -ForegroundColor Green
}

function Clean-PnpmCache {
    Write-Host ""
    Write-Host "--- Cleaning pnpm Cache ---" -ForegroundColor Yellow
    $before = (Get-PSDrive C).Free
    $pnpmCmd = Get-Command pnpm -ErrorAction SilentlyContinue
    if ($pnpmCmd) {
        pnpm store prune 2>&1 | Out-Null
    }
    Remove-Item "$env:LOCALAPPDATA\pnpm-cache" -Recurse -Force -ErrorAction SilentlyContinue
    $after = (Get-PSDrive C).Free
    Write-Host "  Reclaimed: $([math]::Round(($after - $before)/1GB,2)) GB" -ForegroundColor Green
}

function Clean-UvCache {
    Write-Host ""
    Write-Host "--- Cleaning uv Cache ---" -ForegroundColor Yellow
    $before = (Get-PSDrive C).Free
    $uvCmd = Get-Command uv -ErrorAction SilentlyContinue
    if ($uvCmd) {
        uv cache clean 2>&1 | Out-Null
    } else {
        Remove-Item "$env:LOCALAPPDATA\uv\cache" -Recurse -Force -ErrorAction SilentlyContinue
        Remove-Item "$env:APPDATA\uv\cache" -Recurse -Force -ErrorAction SilentlyContinue
    }
    $after = (Get-PSDrive C).Free
    Write-Host "  Reclaimed: $([math]::Round(($after - $before)/1GB,2)) GB" -ForegroundColor Green
}

function Clean-GoCache {
    Write-Host ""
    Write-Host "--- Cleaning Go Build Cache ---" -ForegroundColor Yellow
    $before = (Get-PSDrive C).Free
    $goCmd = Get-Command go -ErrorAction SilentlyContinue
    if ($goCmd) {
        go clean -cache 2>&1 | Out-Null
    } else {
        Remove-Item "$env:LOCALAPPDATA\go-build" -Recurse -Force -ErrorAction SilentlyContinue
    }
    $after = (Get-PSDrive C).Free
    Write-Host "  Reclaimed: $([math]::Round(($after - $before)/1GB,2)) GB" -ForegroundColor Green
}

function Compact-DockerVHDX {
    Write-Host ""
    Write-Host "--- Compacting Docker VHDX ---" -ForegroundColor Yellow

    $vhdx = "$env:LOCALAPPDATA\Docker\wsl\disk\docker_data.vhdx"
    if (-not (Test-Path $vhdx)) {
        Write-Host "  Docker VHDX not found. Skipping." -ForegroundColor DarkGray
        return
    }

    # Check if admin
    $isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    if (-not $isAdmin) {
        Write-Host "  ERROR: Requires Administrator privileges. Re-run as Admin." -ForegroundColor Red
        return
    }

    # Check if Docker/WSL is running
    $dockerProcs = Get-Process *docker* -ErrorAction SilentlyContinue
    if ($dockerProcs) {
        Write-Host "  Docker is running. Stopping Docker and WSL..." -ForegroundColor DarkYellow
        Get-Process *docker* -ErrorAction SilentlyContinue | Stop-Process -Force
        Start-Sleep -Seconds 3
        wsl --shutdown 2>&1 | Out-Null
        Start-Sleep -Seconds 3
    }

    $before = (Get-Item $vhdx).Length
    Write-Host "  VHDX before: $([math]::Round($before/1GB,2)) GB"

    # Try Optimize-VHD first, fallback to diskpart
    try {
        Optimize-VHD -Path $vhdx -Mode Full -ErrorAction Stop
    } catch {
        $dpScript = "select vdisk file=`"$vhdx`"`r`nattach vdisk readonly`r`ncompact vdisk`r`ndetach vdisk`r`nexit"
        $dpFile = "$env:TEMP\compact_docker_tmp.txt"
        Set-Content -Path $dpFile -Value $dpScript -Encoding ASCII
        diskpart /s $dpFile 2>&1 | Out-Null
        Remove-Item $dpFile -ErrorAction SilentlyContinue
    }

    $after = (Get-Item $vhdx).Length
    Write-Host "  VHDX after:  $([math]::Round($after/1GB,2)) GB"
    Write-Host "  Reclaimed:   $([math]::Round(($before - $after)/1GB,2)) GB" -ForegroundColor Green
}

function Empty-RecycleBin {
    Write-Host ""
    Write-Host "--- Emptying Recycle Bin ---" -ForegroundColor Yellow
    $before = (Get-PSDrive C).Free
    try {
        Clear-RecycleBin -Force -ErrorAction Stop
    } catch {
        Write-Host "  Could not empty Recycle Bin: $($_.Exception.Message)" -ForegroundColor DarkGray
    }
    $after = (Get-PSDrive C).Free
    Write-Host "  Reclaimed: $([math]::Round(($after - $before)/1GB,2)) GB" -ForegroundColor Green
}

# --- Main Loop ---
$totalBefore = (Get-PSDrive C).Free

while ($true) {
    Show-Menu
    $choice = Read-Host "Select an option"

    switch ($choice.ToUpper()) {
        "1" { Clean-TempFolder }
        "2" { Clean-YarnCache }
        "3" { Clean-NpmCache }
        "4" { Clean-PnpmCache }
        "5" { Clean-UvCache }
        "6" { Clean-GoCache }
        "7" { Compact-DockerVHDX }
        "8" { Empty-RecycleBin }
        "A" {
            Write-Host ""
            Write-Host "Running ALL cleanups..." -ForegroundColor Cyan
            Clean-TempFolder
            Clean-YarnCache
            Clean-NpmCache
            Clean-PnpmCache
            Clean-UvCache
            Clean-GoCache
            Compact-DockerVHDX
            Empty-RecycleBin
        }
        "Q" {
            $totalAfter = (Get-PSDrive C).Free
            Write-Host ""
            Write-Host "========================================" -ForegroundColor Cyan
            Write-Host "  Session total reclaimed: $([math]::Round(($totalAfter - $totalBefore)/1GB,2)) GB" -ForegroundColor Green
            Write-Host "  Current free space: $([math]::Round($totalAfter/1GB,2)) GB" -ForegroundColor Green
            Write-Host "========================================" -ForegroundColor Cyan
            Write-Host ""
            Read-Host "Press Enter to exit"
            return
        }
        default { Write-Host "  Invalid option." -ForegroundColor Red }
    }
}
