---
created: 2026-05-07
tags:
  - kb
  - powershell
  - windows
---

# PowerShell Environment Variables

## Set Environment Variable

```powershell
[Environment]::SetEnvironmentVariable('KEY', 'VALUE', [EnvironmentVariableTarget]::User)
```

## Get Environment Variable

```powershell
[Environment]::GetEnvironmentVariable('KEY', [EnvironmentVariableTarget]::User)
```

## Delete Environment Variable

```powershell
[Environment]::SetEnvironmentVariable('KEY', $null, [EnvironmentVariableTarget]::User)
```

## Sources

- [What is PowerShell? (docs.microsoft.com)](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)

Note Created: 2026-05-07
