---
id: 93wlhx7u9ua7pz3wma2l597
title: PowerShell
desc: ''
updated: 1705151526550
created: 1705151315288
tags:
    - powershell
    - windows
---

* Source:
  * [Reset a user password with PowerShell (4sysops.com)](https://4sysops.com/archives/powershell-password-resets/)
  *  [What is PowerShell? (docs.microsoft.com)](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)


```powershell
$newpwd = Read-Host "Enter the new password" -AsSecureString
Set-ADAccountPassword jfrost -NewPassword $newpwd -Reset -PassThru | Set-ADuser -ChangePasswordAtLogon $True

```

```powershell

get-aduser -filter "department -eq 'marketing' -AND enabled -eq 'True'"
get-aduser -filter "department -eq 'marketing' -AND enabled -eq 'True'" | Set-ADAccountPassword -NewPassword $newpwd -Reset -PassThru | Set-ADuser -ChangePasswordAtLogon $True
get-aduser -filter "department -eq 'marketing' -AND enabled -eq 'True'" | Set-ADuser -ChangePasswordAtLogon $True
```
