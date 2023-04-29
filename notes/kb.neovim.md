---
id: wfa0ezuoa81eppr89q46yac
title: Neovim
desc: ''
updated: 1682756866056
created: 1682755423382
tags:
  - kb
  - tool
  - vim
  - nvim
  - neovim
  - windows
---

## NeoVIM on Windows

### Install NeoVIM

```powershell
winget install -e --id Neovim.Neovim
```

### Configure NeoVIM

Configuration files are in: `%LOCALAPPDATA%\nvim\init.vim`

Data is in:
  `%LOCALAPPDATA%\nvim-data\`
that means you clode e.g. `packer` to:
  `git clone --depth 1 https://github.com/wbthomason/packer.nvim site/pack/packer/start/packer.nvim`
