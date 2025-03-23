.. _inbox:

=====
Inbox
=====

Famous People
=============

* Hedy Lamarr -- fled from abuse;
  became a world famous actress and, just because she could,
  invented a carbonated drink and
  sprinkled on top a wireless/radio torpedo guidance system
  for the allied forces in WW2
  (some say is the basis for bluetooth/wireless connections today)
* Katherine Johnson
  -- calculated the trajectory for the flight of first American in space
  Alan Shepard (not sure about that part, I believe she did it with pen & paper)
* the NASA computers -- hired in the 1930s to, literally,
  compute complex calculations.
  (This is, if I remember correctly, where the term computer originates from).

Quotes
======

.. epigraph::

  A jack of all trades
  Is a master of none,
  But still always better
  Than a master of one!

  -- (Unknown;
  possibly in reference to William Shakespeare;
  <https://en.wiktionary.org/wiki/jack_of_all_trades,_master_of_none#English>)

.. epigraph::

  Great minds think alike,
  but fools rarely differ!

  -- (Unknown; proverb)

``pandoc``
==========

Convert a `docx` file to `md`:

.. code-block:: powershell
  :linenos:

  &pandoc `
   --verbose `
   --from docx `
   --to markdown `
   --default-image-extension=png `
   --extract-media=images `
   'document.docx' -o document.md

Code Design
===========

Functional Core, Imperative Shell
---------------------------------

* [Functional Core, Imperative Shell (destroyallsoftware.com)](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell)
* [Robert C Martin - Functional Programming; What? Why? When? (youtube.com)](https://www.youtube.com/watch?v=7Zlp9rKHGD4)
* [Moving IO to the edges of your app: Functional Core, Imperative Shell - Scott Wlaschin (youtube.com)](https://www.youtube.com/watch?v=P1vES9AgfC4)

.. code-block:: mermaid
  :linenos:

  journey
     title Functional Core, Imperative Shell
     section Side Effects (Imperative Shell)
      I/O: 3: Developer
      Validation: 3: Developer
     section Pure (Functional Core)
      Business Logic: 4: Developer
     section Side Effects (Imperative Shell)
      Validation: 3: Developer
      I/O: 3: Developer

Jenkins Snippets
----------------

.. code-block:: groovy
  :linenos:

  // This was the only script that allowed me to see the zombie job
  jenkins.model.Jenkins.instance.computers.collect { c -> c.executors }.collectMany { it.findAll { it.isBusy () } }.each { it -> println(it.getName()); }

  // Try to stop it but didn't work
  jenkins.model.Jenkins.instance.computers.collect { c -> c.executors }.collectMany { it.findAll { it.isBusy () } }.each { it.stop () }

.. code-block:: groovy
  :linenos:

  Jenkins.instance.getItemByFullName("example-folder/example-job-name").getBuildByNumber(69).finish(hudson.model.Result.ABORTED, new java.io.IOException("Aborting build"));

.. code-block:: groovy
  :linenos:

  Jenkins.instance.getItemByFullName("example-folder/example-job-name").getBuildByNumber(420).finish(hudson.model.Result.ABORTED, new java.io.IOException("Aborting build"));

Games
=====

Dyson Sphere Program (DSP)
--------------------------

* `Dyson Sphere Program Tools <https://factoriolab.github.io/dsp>`_
