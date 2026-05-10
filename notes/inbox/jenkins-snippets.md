---
created: 2026-05-07
id: 8a9b8cee-3eae-4251-a5d9-7b5969bac56d
tags:
  - misc
  - kb
title: Jenkins Snippets
---

# Jenkins Snippets

```groovy
// This was the only script that allowed me to see the zombie job
jenkins.model.Jenkins.instance.computers.collect { c -> c.executors }.collectMany { it.findAll { it.isBusy () } }.each { it -> println(it.getName()); }

// Try to stop it but didn't work
jenkins.model.Jenkins.instance.computers.collect { c -> c.executors }.collectMany { it.findAll { it.isBusy () } }.each { it.stop () }
```

``` groovy
Jenkins.instance.getItemByFullName("example-folder/example-job-name").getBuildByNumber(69).finish(hudson.model.Result.ABORTED, new java.io.IOException("Aborting build"));
```

``` groovy
Jenkins.instance.getItemByFullName("example-folder/example-job-name").getBuildByNumber(420).finish(hudson.model.Result.ABORTED, new java.io.IOException("Aborting build"));
```
