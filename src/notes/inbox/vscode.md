---
created: 2026-05-07
id: 8ddf960e-68ee-4122-91ab-2ecd4458729c
tags:  \[misc\]
---

# VS Code

- part of [*editor\|editors*]

## [[docker]] mounts `wayland-0` on Windows

Recent versions of the [Dev Containers
ms-vscode-remote.remote-containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
extension introduce a new setting. This setting tries to detect whether
it can mount a socket \"`wayland-0`\". This detection fails
with `fedoraremix`. The setting below disables this detection
and removes the automatic mount from the docker command that starts the
container.

``` json
{
  "dev.containers.mountWaylandSocket": false
}
```

## Clean Up

``` powershell
Remove-Item -Recurse -Force $env:LOCALAPPDATA\vscode-sqltools\
Remove-Item -Recurse -Force $env:USERPROFILE\.vscode\
Remove-Item -Recurse -Force $env:APPDATA\Code
Remove-Item -Recurse -Force $env:USERPROFILE\.vscode
```

## Extensions

Using `git worktree`:

- [Git Worktree (Phil
  Stainer)](https://marketplace.visualstudio.com/items?itemName=PhilStainer.git-worktree)
- [Git Worktree (Git
  Worktrees)](https://marketplace.visualstudio.com/items?itemName=GitWorktrees.git-worktrees)
