---
id: j3v4tam0s8xb5fesww63d4l
title: Managing Go Installations
desc: ''
updated: 1716160285324
created: 1716159866461
tags:
  - go
---

* [Managing Go installations - The Go Programming Language](https://go.dev/doc/manage-install)

## Install Go versions

```shell-session
~> go install golang.org/dl/go1.21.10@latest
~> go1.21.10 env
go1.21.10: not downloaded. Run 'go1.21.10 download' to install to ...
~> go1.21.10 download
Downloaded   0.0% (    3124 / 73785140 bytes) ...
Downloaded   1.0% (  720896 / 73785140 bytes) ...
Downloaded  24.6% (18152768 / 73785140 bytes) ...
Downloaded  47.3% (34914048 / 73785140 bytes) ...
Downloaded  70.7% (52166272 / 73785140 bytes) ...
Downloaded  96.7% (71384544 / 73785140 bytes) ...
Downloaded 100.0% (73785140 / 73785140 bytes)
Unpacking ...
Success. You may now run 'go1.21.10'
~> go1.21.10 env     
set GO111MODULE=
...
```
