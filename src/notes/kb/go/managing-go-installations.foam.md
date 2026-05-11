---
created: 2026-05-07
tags:
  - kb
  - go
---

# Managing Go Installations

## Installing Go on Linux

```bash
curl -L -O https://go.dev/dl/go1.26.3.linux-amd64.tar.gz
mkdir -p $HOME/sdk
sudo tar -C $HOME/sdk -xzf go1.26.3.linux-amd64.tar.gz
# strip leading tabs, don't expand variables, and don't interpret backslashes
cat <<-'EOF' >> $HOME/.bashrc.d/go.sh
  # Go environment
  if ! [[ "$PATH" =~ "$HOME/sdk/go/bin" ]]; then
      PATH="$HOME/sdk/go/bin:$PATH"
  fi
  export PATH

  if ! [[ "$PATH" =~ "$HOME/go/bin" ]]; then
      PATH="$HOME/go/bin:$PATH"
  fi
  export PATH
EOF
```

## Install Go versions

- Using CGO requires _Development Tools_ to be installed on Fedora (and likely other distros as well)
  - see [Fedora Development Tools](./fedora-development-tools/note.foam.md)

```console
go install golang.org/dl/go1.21.10@latest
```

```console
$ go1.21.10 env
go1.21.10: not downloaded. Run 'go1.21.10 download' to install to ...
```

```console
$ go1.21.10 download
Downloaded   0.0% (    3124 / 73785140 bytes) ...
Downloaded   1.0% (  720896 / 73785140 bytes) ...
Downloaded  24.6% (18152768 / 73785140 bytes) ...
Downloaded  47.3% (34914048 / 73785140 bytes) ...
Downloaded  70.7% (52166272 / 73785140 bytes) ...
Downloaded  96.7% (71384544 / 73785140 bytes) ...
Downloaded 100.0% (73785140 / 73785140 bytes)
Unpacking ...
Success. You may now run 'go1.21.10'
```

```console
$ go1.21.10 env
set GO111MODULE=
...
```

## Sources

- [Managing Go installations - The Go Programming
  Language](https://go.dev/doc/manage-install)
