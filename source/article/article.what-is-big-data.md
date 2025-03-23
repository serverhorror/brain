# What is big data?

It's actually quite simple: You have big data whenever a single host isn't enough to either store or process your data.

What does it mean?  
Suppose you have a Postgresql Database and you run into scaling problems. There's a choice now, either get ΓÇ£betterΓÇ¥ hardware so that you can continue to work on a single host or split the database to span multiple hosts.

Suppose you have a file store and all disks are full. You can either buy larger disks or use some distributed storage system where you just add hosts to expand the total storage capacity.

*In both cases you are dealing with big data.*

Big data (for me) isn't anything that says *X MB of data*. It's simply the case *when you ~~need~~ decide to use a distributed system to handle your data*.  
*/serverhorror*
