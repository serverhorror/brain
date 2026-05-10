---
created: 2026-05-07
tags:
  - kb
  - git
  - go
---

# Git

## Using **BitBucket Server/Datacenter** Git

1. Create a personal access token

2. Do this for your git configuration

    ```bash
    git config --global http.https://bitbucket.example.com.extraHeader 'Authorization: Bearer  Token'
    ```

    Some more details

    ```bash
    git clone -c http.extraHeader='Authorization: Bearer REPLACE_WITH_TOKEN' https://bitbucket.example.com/scm/project-name/repo-name.git
    git config --global http.https://bitbucket.example.com.extraHeader 'Authorization: Bearer  Token'
    ```

    *or* (if you don\'t want to use the token in the header)

    ```bash
    git config --global url."https://<username>:<personal-access-token>@bitbucket.example.com".insteadOf "https://bitbucket.example.com"
    ```

3. As your module URLs use something like this for [[go/note.foam.md]] projects:

    - `bitbucket.example.com/project/repo`

      **Do NOT** use the `scm` part in the URL

[go/note.foam.md]: note.foam.md "Go"
