# PowerShell script to organize files into folders based on their name

# Get the current directory where the script is located
$currentDirectory = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Get all files in the current directory (excluding directories and the script itself)
$filesToOrganize = Get-ChildItem -Path $currentDirectory -File | Where-Object { $_.Name -ne "group_files_by_name.ps1" }

foreach ($file in $filesToOrganize) {
    # Get the base name of the file (without extension)
    $folderName = $file.BaseName

    # Construct the full path for the new folder
    $newFolderPath = Join-Path -Path $currentDirectory -ChildPath $folderName

    # Create the new folder if it doesn't exist
    if (-not (Test-Path $newFolderPath)) {
        New-Item -ItemType Directory -Path $newFolderPath | Out-Null
        Write-Host "Created folder: $newFolderPath"
    }

    # Construct the full path for the destination file
    $destinationFilePath = Join-Path -Path $newFolderPath -ChildPath $file.Name

    # Move the file into the new folder
    Move-Item -Path $file.FullName -Destination $destinationFilePath -Force
    Write-Host "Moved '$($file.Name)' to '$newFolderPath'"
}

Write-Host "File organization complete."
