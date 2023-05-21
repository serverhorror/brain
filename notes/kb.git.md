---
id: x4pn71mwd404ce9lxmdfonf
title: Git
desc: ''
updated: 1684701125414
created: 1670682312698
tags:
  - git
  - go
  - kb
---

## Using **BitBucket Server** with Go and Git

1. Create a personal access token
1. Do this for your git configuration
   ```text
   git config --global url."https://<username>:<personal-access-token>@bitbucket.example.com".insteadOf "https://bitbucket.example.com"
   ```
1. As your module URLs use something like this:
   * `bitbucket.example.com/project/repo`

     **Do NOT** use the `scm` part in the URL
