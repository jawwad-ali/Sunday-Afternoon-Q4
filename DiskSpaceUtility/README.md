# Disk Space Utility

Two PowerShell scripts to investigate and clean up disk space on Windows.

## Scripts

| Script | Purpose |
|---|---|
| `DiskSpaceInvestigator.ps1` | Scans your system and reports what's consuming disk space |
| `DiskSpaceCleaner.ps1` | Interactive menu to selectively clean up space |

## What the Cleaner Can Clean

| Option | What it cleans |
|---|---|
| 1 | User Temp folder (V8 .node cache files, old installers, etc.) |
| 2 | Yarn cache |
| 3 | npm cache + _npx |
| 4 | pnpm cache + store |
| 5 | uv (Python) cache |
| 6 | Go build cache |
| 7 | Compact Docker VHDX virtual disk (requires Admin) |
| 8 | Empty Recycle Bin |
| A | All of the above |

All items cleaned are caches — they will be re-downloaded automatically when needed (e.g. on your next `npm install` or `yarn install`).

## How to Run

### Method 1 — Right-Click

1. Open the `DiskSpaceUtility` folder on your Desktop
2. Right-click on the script (e.g. `DiskSpaceCleaner.ps1`)
3. Select **Run with PowerShell**

### Method 2 — From Terminal (PowerShell, CMD, or Git Bash)

**Investigator (scan only):**

```
powershell -ExecutionPolicy Bypass -File "C:\Users\Ali\Desktop\DiskSpaceUtility\DiskSpaceInvestigator.ps1"
```

**Cleaner (interactive menu):**

```
powershell -ExecutionPolicy Bypass -File "C:\Users\Ali\Desktop\DiskSpaceUtility\DiskSpaceCleaner.ps1"
```

### Running as Administrator (required for Docker VHDX compaction)

1. Open the Start Menu and search for **PowerShell**
2. Right-click on **Windows PowerShell** and select **Run as Administrator**
3. Run the following command:

```
powershell -ExecutionPolicy Bypass -File "C:\Users\Ali\Desktop\DiskSpaceUtility\DiskSpaceCleaner.ps1"
```

Then select option **7** to compact the Docker VHDX.

## Notes

- The `-ExecutionPolicy Bypass` flag is needed because Windows blocks unsigned scripts by default. It only applies to that single run and does not change your system settings.
- Docker and WSL must be fully stopped before compacting the VHDX. The script handles this automatically when run as Admin.
- The Investigator script is read-only — it does not modify or delete anything.
- The Cleaner shows live sizes next to each option and reports how much space was reclaimed after each cleanup.
