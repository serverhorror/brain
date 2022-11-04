---
id: nutu4yqw6s7bst20gm794xs
title: Misc
desc: ''
updated: 1666864287540
created: 1665437949507
---

## Misc

```mermaid
%%{ init: { 'flowchart': { 'curve': 'monotoneX' } } }%%
graph LR

dockerfile[/Dockerfile/]
containerfile[/Containerfile/]

podman_build[podman]
docker_build[docker]

image(Image)
container[/Container/]


subgraph build
  direction LR
  docker_build
  podman_build
end

containerfile-->podman_build
dockerfile-->podman_build
dockerfile-->docker_build

subgraph runtime
container
end

podman_build & docker_build-->image-->container
```
