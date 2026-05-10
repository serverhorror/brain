---
created: 2026-05-07
tags:
  - kb
  - powershell
  - windows
---

# PowerShell Password Reset

## Reset password for users in a certain field and force password reset

```powershell
get-aduser -filter "department -eq 'marketing' -AND enabled -eq 'True'" | Set-ADAccountPassword -NewPassword $newpwd -Reset -PassThru | Set-ADuser -ChangePasswordAtLogon $True
```

## Force password reset for users in a certain field

```powershell
get-aduser -filter "department -eq 'marketing' -AND enabled -eq 'True'" | Set-ADuser -ChangePasswordAtLogon $True
```

## Sources

- [Reset a user password with PowerShell (4sysops.com)](https://4sysops.com/archives/powershell-password-resets/)

Note Created: 2026-05-07
