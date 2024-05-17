---
id: x4pn71mwd404ce9lxmdfonf
title: Git
desc: ''
updated: 1715967816699
created: 1670682312698
tags:
  - git
  - go
  - kb
  - bitbucket
---

## Using **BitBucket Server/Datacenter** Git

1. Create a personal access token
1. Do this for your git configuration
   ```text
   git config --global url."https://<username>:<personal-access-token>@bitbucket.example.com".insteadOf "https://bitbucket.example.com"
   git clone -c http.extraHeader='Authorization: Bearer REPLACE_WITH_TOKEN' https://bitbucket.example.com/scm/project-name/repo-name.git
   git config --global http.https://bitbucket.example.com.extraHeader 'Authorization: Bearer  Token'
   ```
1. As your module URLs use something like this for [[kb.go]] projects:
   * `bitbucket.example.com/project/repo`

     **Do NOT** use the `scm` part in the URL
