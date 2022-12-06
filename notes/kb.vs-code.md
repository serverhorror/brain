---
id: iyfe99prifkm2956srumpqk
title: Vs Code
desc: ''
updated: 1670318368127
created: 1663335829621
---

## Clean Up

```powershell
Remove-Item -Recurse -Force $env:LOCALAPPDATA\vscode-sqltools\
Remove-Item -Force -Recurse $env:USERPROFILE\.vscode\
Remove-Item -Recurse -Force $env:APPDATA\Code
Remove-Item -Recurse -Force $env:USERPROFILE\.vscode
```
