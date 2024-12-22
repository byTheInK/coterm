$RepoUrl = "https://github.com/byTheInK/coterm" #Github repo
$InstallPath = "$env:USERPROFILE\repos\coterm" # Install Path

# Function to check if script is running as administrator
function Check-Administrator {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    Write-Host $currentUser
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# Function to check if software is installed
function Is-SoftwareInstalled($name) {
    Get-Command $name -ErrorAction SilentlyContinue | ForEach-Object { return $true }
    return $false
}

# Function to download files using BitsTransfer
function Download-File($url, $outputPath) {
    Write-Host "Downloading $url to $outputPath..."
    Start-BitsTransfer -Source $url -Destination $outputPath -ErrorAction Stop
}

# Download and install Python if not installed
if (-not (Is-SoftwareInstalled -name "python")) {
	Write-Host "Please install the latest Python version and if not add It to the Path."
} else {
    Write-Host "Python is already installed."
}

# Download and install Git if not installed
if (-not (Is-SoftwareInstalled -name "git")) {
	Write-Host "Please install the latest Git version and if not add It to the Path."
} else {
    Write-Host "Git is already installed."
}

# Clone the GitHub repository
if (!(Test-Path -Path $InstallPath)) {
    Write-Host "Cloning repository $RepoUrl..."
    git clone $RepoUrl $InstallPath
} else {
    Write-Host "Repository already cloned. Skipping clone."
}

# Add the cloned repository to PATH
$CurrentPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)
if (-not (Check-Administrator)) {
    Write-Host "Running without administrator privileges. Updating PATH for the current user."
    $CurrentPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::User)
    if ($CurrentPath -notlike "*$InstallPath*") {
        Write-Host "Adding $InstallPath to user PATH..."
        [System.Environment]::SetEnvironmentVariable("Path", "$CurrentPath;$InstallPath", [System.EnvironmentVariableTarget]::User)
        Write-Host "PATH updated for the current user. Restart your session to apply changes."
    } else {
        Write-Host "$InstallPath is already in user PATH."
    }
} else {
    if ($CurrentPath -notlike "*$InstallPath*") {
        Write-Host "Adding $InstallPath to system PATH..."
        [System.Environment]::SetEnvironmentVariable("Path", "$CurrentPath;$InstallPath", [System.EnvironmentVariableTarget]::Machine)
        Write-Host "PATH updated system-wide. Restart your session to apply changes."
    } else {
        Write-Host "$InstallPath is already in system PATH."
    }
}
