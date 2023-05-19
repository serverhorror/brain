---
id: iyfe99prifkm2956srumpqk
title: Vs Code
desc: ''
updated: 1684518491553
created: 1663335829621
---

## Docker mounts `wayland-0` on Windows

Recent versions of the 
```json
{
    "dev.containers.mountWaylandSocket": false
}
```

## Clean Up

```powershell
Remove-Item -Recurse -Force $env:LOCALAPPDATA\vscode-sqltools\
Remove-Item -Recurse -Force $env:USERPROFILE\.vscode\
Remove-Item -Recurse -Force $env:APPDATA\Code
Remove-Item -Recurse -Force $env:USERPROFILE\.vscode
```
