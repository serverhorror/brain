---
id: uly1rz3619dy10urzw1kpnv
title: Server!/Horror!
desc: ''
updated: 1705577272255
created: 1665428988423
---

This just exists to quickly go the the published page:

* http://serverhorror.github.io/brain

## Interesting Texts

* [[misc.rules]]
* [[misc.as-a-software-developer]]
* [[misc.secrets-in-systems-engineering]]

## Knowledge Base

* [[kb]]

## Random notes that are not yet sorted

### Write yourself a Git!

Source:

  * https://wyag.thb.lt/

    Uses #Python to implement basic [[Git|tags.git]] functionality.

### Note Taking

* Alternative to Dendron: [Foam (foambubble.github.io)](https://foambubble.github.io/foam)
  * https://foambubble.github.io/foam/user/getting-started/recommended-extensions

### instruqt

* https://instruqt.com/

Looks like it could be a good way to learn new things.
The platform provides more server side functionality than e.g. [[kb.hackerrrank]] or [[kb.codewars]].

### SadServers

* https://sadservers.com/
* https://github.com/fduran/sadservers

### Google AIPs

* https://google.aip.dev/

## Games

### Dyson Sphere Program (DSP)

* https://factoriolab.github.io/dsp

## Lookup

This section contains useful links to related resources.

* [Getting Started Guide](https://link.dendron.so/6b25)
* [Discord](https://link.dendron.so/6b23)
* [Home Page](https://wiki.dendron.so/)
* [Github](https://link.dendron.so/6b24)
* [Developer Docs](https://docs.dendron.so/)

## Install Visual Studio 2022 Build Tools

```powershell
inget install -e `
  --id Microsoft.VisualStudio.2022.BuildTools `
  --override "--wait --quiet --add ProductLang En-us --add Microsoft.VisualStudio.Workload.NativeDesktop --includeRecommended"
```

## Jenkins Snippets


```groovy
// This was the only script that allowed me to see the zombie job
jenkins.model.Jenkins.instance.computers.collect { c -> c.executors }.collectMany { it.findAll { it.isBusy () } }.each { it -> println(it.getName()); }

//Try to stop it but didnt work
jenkins.model.Jenkins.instance.computers.collect { c -> c.executors }.collectMany { it.findAll { it.isBusy () } }.each { it.stop () }
```

```groovy
Jenkins.instance.getItemByFullName("example-folder/example-job-name").getBuildByNumber(69).finish(hudson.model.Result.ABORTED, new java.io.IOException("Aborting build"));
```

```groovy
Jenkins.instance.getItemByFullName("example-folder/example-job-name").getBuildByNumber(420).finish(hudson.model.Result.ABORTED, new java.io.IOException("Aborting build"));
```
