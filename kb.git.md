---
title: Git
tags:
  - git
  - tools
  - kb
---

## Using **BitBucket Server/Datacenter** Git

1. Create a personal access token
1. Do this for your git configuration

   ```text
   git config --global http.https://bitbucket.example.com.extraHeader 'Authorization: Bearer  Token'
   ```

   Some more details

   ```text
   git clone -c http.extraHeader='Authorization: Bearer REPLACE_WITH_TOKEN' https://bitbucket.example.com/scm/project-name/repo-name.git
   git config --global http.https://bitbucket.example.com.extraHeader 'Authorization: Bearer  Token'
   ```

   **OR** (if you don't want to use the token in the header)

   ```text
   git config --global url."https://<username>:<personal-access-token>@bitbucket.example.com".insteadOf "https://bitbucket.example.com"
   ```

1. As your module URLs use something like this for [[kb.go]] projects:

   - `bitbucket.example.com/project/repo`

     **Do NOT** use the `scm` part in the URL

[kb.go]: kb.go.md "Go"
