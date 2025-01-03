---
id: wfa0ezuoa81eppr89q46yac
title: NeoVIM
desc: ""
updated: 1716160972880
created: 1682755423382
tags:
  - kb
  - tools
  - windows
---

## Using the system clipboard

```vim
"*y -- yank to system clipboard
"+p -- paste from system clipboard
```

## NeoVIM on Windows

### Install NeoVIM

```powershell
winget install -e --id Neovim.Neovim
```

### Configure NeoVIM

- let NeoVIM tell where it will look for the config

```
:echo stdpath('config')
```

Configuration files are in: `%LOCALAPPDATA%\nvim\init.vim`

Data is in:
`%LOCALAPPDATA%\nvim-data\`
that means you clone e.g. `packer` to:
`git clone --depth 1 https://github.com/wbthomason/packer.nvim site/pack/packer/start/packer.nvim`
