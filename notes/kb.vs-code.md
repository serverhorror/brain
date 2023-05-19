---
id: iyfe99prifkm2956srumpqk
title: Vs Code
desc: ''
updated: 1684518677178
created: 1663335829621
---

## Docker mounts `wayland-0` on Windows

Recent versions of the "[_Dev Containers_ `ms-vscode-remote.remote-containers`](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)" extension introduce a new setting.
This setting tries to detect whether it can mount a socket "`wayland-0`".
This detection fails with `fedoraremix`.
The setting below disables this detection and removes the automatic mount from the docker command that starts the container.

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
