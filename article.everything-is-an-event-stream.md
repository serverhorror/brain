# Everything is a fucking event stream

I got quite fed up with monitoring systems lately. **I do not see a need for such systems any more**, and I hate to introduce yet another component that does not actually add any value!

No go away and turn around and read something else if you think this is utter bullshit, but recently I took some time to think about what a monitoring system actually does.

In my opinion a monitoring system is nothing more that a logging system. You generate some *log message (which actually isn't a log message)* and send it off to a central host (possibly with several level of intermediate hosts) just to fire off a notification your *log message.*

So what do we have? We have a log stream! But since I don't actually really care about log messages let's generalize a bit and **call everything an event!**

## **Everything is a fucking event stream!**

**I do mean everything!**

Let's begin with syslog (yup classic syslog, no bells and whistles). Have you ever thought about what the separation marker for a syslog event is? I don't know for sure what it is. For a long time I thought that the only true answer would be a newline.

Hey, *who the hell wants to read Java stack traces in a log file* or Python or any ΓÇ£multi line messageΓÇ¥.

**I do!**

Of course I don't want to use grep or less or anything to work through those files. I want a tool that understands those messages. Better yet I want a tool that is usable and that let's me define reusable rules to tag *~~log messages~~* **events.**

Think of Nagios:

you write some plug-in, the plug-in has a log, the plug-in reports to stdout for Nagios messages, the plug-in writes to stderr to tell about errors, there are different levels of verbosity to debug, it has at least 2 different return values

Why on earth is there:

a stream of plugin results (usually exit codes), a stream of messages on stdout (*meta results?*), a stream of log messages (meta2 *results?*), a stream of messages for stderr (is that logging, monitoring, meta3 results, ignorable?)

On top of that all those kinds of messages are incompatible. **There's no such thing as structured logging!**

Please, please just let me send everything to some remote place where it will be persisted and I have a central view on all my events.

Add as much meta data as possible.

source host, receiving host (or hosts if there were several in between), reception times, timestamps (**and please: do add fractions of a second**), **hostnames and ip addresses,** a possibility to extend the amount of meta data

Now when I have a place where I can look at all my events, then and only then I want to make decisions about what I'm interested in. I'm nowhere near deciding on whether any of this is an alert.

## **After the fact tagging**

Nagios, Icinga, Zabbix all force me to make something up. Some test, a probe or whatnot where I have to write some script (Don't get me wrong: I like scripting \-- scripting takes away those repetitive tasks I hate!) and make up arbitrary values that represent a certain level of goodness or badness. OK, CRITICAL, WARNING?

WTF? Who said I need three of them?

Just let me define some criteria that will match events. Please note that I am not restricting the criteria to regular expressions. Something like ΓÇ£Has the meta data field XΓÇ¥, ΓÇ£Does not have meta data field YΓÇ¥, ΓÇ£After January 1st 1992 but not before May 3rd 1982ΓÇ¥, ΓÇ£Only between 13:00h and and 13:15h when the load was higher than 3 on systems with with only 2 coresΓÇ¥ and so on. Those are equally important.

*Uh, oh! I just defined some plug-ins, now I'm back at monitoring!* ***No I'm not!***

I ran a cron job (in the simplest case) that generated an event which told me the load, and another cron job that told me the number of cores in the system. These events were sent to my event sink for later processing!

I need to be able to save those criteria collections as filters/view or whatever you want to call them and I need to be able to name those things so that I can find them later on. I simply want to label my events.

I need to be able to attach as many labels to events as I see fit. Also I need the ability to find unlabeled events.

## **Which brings us to alerts!**

So now that I know what's interesting and gives me the ability to make educated decisions about what's actually interesting I can decide on when it's worth to raise something that will wake me up in the middle of the night.

I do want to be able to generate alerts and send them to some other system...

**Hey look! Another event stream!**

...and then I'd rather not want to specify when things go bad. I'd rather would like to specify when things are good. Everything else is just **badness enumeration**.

I'd rather triple the amount of time I invest in such a system than to create yet another monitoring system that doesn't use what's already there.

## **But today's alerts aren't worth anything tomorrow!**

Any system that silently throws away data is useless (I'm looking at you Munin and friends). I'm not saying RRDtool is a bad thing. I love it, the problem is how people use it.

Throw away data? Come on, who wants this? I do want to the finest possible resolution, we have Hadoop, GlusterFS, Ceph. Storage is something that shouldn't be in the way. I'd rather have only 7 days of data than a year of useless junk.

Of course there's trends over long periods of time but those shouldn't be the default, those should be something that are added on top of existing data!

How are today's alerts helpful if I can't possibly tell what happened yesterday between 15:03h and 15:07h?

## **Yes this actually is basic stuff**

**But it's just a syslog server and some scripts!**

Yup you are absolutely right, and that's the reason why companies like Splunk and Loggly make money right? Because anyone just has stuff like that. It's a default, no more to-dos, nothing to see just go along!

Ah so you don't actually have it? Neither do I. But I'd love to! Please someone skilled create such a system and make it open source!

**On top of that: make it near real time!**

*/serverhorror*
