---
title: PowerShell
tags:
  - kb
  - powershell
  - windows
---

- Source:
  - [Reset a user password with PowerShell (4sysops.com)](https://4sysops.com/archives/powershell-password-resets/)
  - [What is PowerShell? (docs.microsoft.com)](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)

```powershell
$newpwd = Read-Host "Enter the new password" -AsSecureString
Set-ADAccountPassword jfrost -NewPassword $newpwd -Reset -PassThru | Set-ADuser -ChangePasswordAtLogon $True
```

```powershell
# Filter users by a certain field
get-aduser -filter "department -eq 'marketing' -AND enabled -eq 'True'"
```

```powershell
# Reset password for users in a certain field and force password reset
get-aduser -filter "department -eq 'marketing' -AND enabled -eq 'True'" | Set-ADAccountPassword -NewPassword $newpwd -Reset -PassThru | Set-ADuser -ChangePasswordAtLogon $True
```

```powershell
# Force password reset for users in a certain field
get-aduser -filter "department -eq 'marketing' -AND enabled -eq 'True'" | Set-ADuser -ChangePasswordAtLogon $True
```
