# Naming Schemas

I've recently been thinking about our naming scheme in the company, up until now it has worked quite well and still does so. With about 300 devices (and growing) I thought I might share this to eventually get some input (if anyone ever reads this, if not I do have some reference at least).

## Domains

We are actively distinguishing between internally and externally available services, one of the easiest ways to remember is to use another domain for internal services than the one you use for external services. There's however the drawback of typing, you can of course configure completely different domains but that is something I consider bad use, you either have to

* buy yet another domain (and never ever use it in public) or  
* ~~use an invalid domain \- [check the corresponding RFC on the proper names](http://www.faqs.org/rfcs/rfc2606.html)~~ This recommendation is deprecated  
* ~~use some random domain and hope you never want to go there or do business with them because it probably would require reconfigurinig all of your machines~~

The option I prefer is to use a dedicated subdomain. Yes that involves some more typing but you can always choose a really short name, **good options I'd consider are**:

* in.example.com  
* int.example.com  
* local.example.com (already quite a bit long)

bad options would be:

* internal.example.com  
* not-public.example.com

Going the other way around and having a dedicated domain for external services while defaulting to internal services isn't quite working because all your customers would have some additional typing consider this:

* blog.public.example.com  
* <www.public.example.com>

Not quite what you want

## Split Horizon DNS

Deserves some paragraph on it's own :)

Split horizon is a technique that is able to give you different answers for the same hostname depending on the source of the request. It may be of use but I don't think it's that good to seperate services with it. How so? Consider the following situation:

You are at your company and visit blog.example.org to publish which is an internal only service, now you go home and remember that you forgot to add some important information, you go to blog.example.org and it just won't work. Heck why? You know the DNS works because just about an hour earlier you were happily typing, you start investigating search stuff and after all you just created unnecessary work for you.

I still consider a simple int.example.org to be better because not only you will know instantly about internal vs. external services but also all your users. And your job is all about giving good services to your users isn't it?

## Hostnames

This is actually more interesting than domains because you and your customers (users and paying customers) will be typing them all day long. There are a few documents that may be helpful:

* [http://tools.ietf.org/html/rfc1178](http://tools.ietf.org/html/rfc1178)  
* [http://tools.ietf.org/html/rfc2100](http://tools.ietf.org/html/rfc2100)  
* [http://www.namingschemes.com/Main\_Page](http://www.namingschemes.com/Main_Page)

Those naming schemes mostly refer to mythology, movies or tv series. All of them are quite well known and try to create a mental link between the meaning of a character, god or creature and the use of the server. Personally however I don't quite like this. It implies knowledge about cultural things that may not quite apply depending on where you are located.

We have a couple of rules that apply to our naming scheme:

* all devices adhere to the same schema (printers, switches, routers, servers, workstations, ...)  
* hostnames are set up from either 2 to 4 parts these are  
* company abbreviation \- max. 3 letters  
* optional environment abbreviation \- a fixed list  
* usage abbreviation (abbreviated only if too long or if usage is still clear)  
* if it is a service that end users should use it will have an internal name with the abbreviation "*vip*" after the environment abbreviation  
* name parts are separated by dashes

### Examples

### Company Abbreviations

* Snake Oil Lt. would become *sno*  
* Bogus Inventory would become *boi*

### Environment Abbreviations

This is fixed in our case we use the following:

* *devl* for development environments \- Developers playground, we don't care about what happens on those boxes, we only provide daily backups  
* *stag* for staging \- Our playground, where we \- SysAdmins \- try to get the config right for a production deployment  
* *prod* for production \- In a perfect world *prod* matches *stag* at all times

### Usage Abbreviations

This is a bit tougher. There's no hard rule but rather something that makes it clear what the box actually does:

* mail \- a mail server with services like imap, smtp or whatever is needed for a mail structure that end users see  
* mailout \- guess what  
* openxdb \- any ideas? [OpenX](http://www.openx.org/) is an ad-server, you can probably imagine what DB stands for. Note that we do not include the type of DB here, that kind of information is something you can figure out as soon as you are on the host or by reading internal documentation

### Putting it all together

Ok, so now we have a couple of rules to apply to our hostnames. Let's say we are going to put up a new project and it requires

* a source code repository (deployed on it's own virtualized server)  
* mailing infrastructure \- fitted to the environment in question, after all we don't want to send out 200.000 test mails to real customers but rather to a certain mailbox the devs can check  
* shared storage to place images  
* a static webhost  
* a database server  
* a webhost with the application itself  
* the company responsible is Snake Oil Ltd.

Let's create the hostnames we are going to use:

* sno-scm.in.snakeoil.example \- note I'm using .invalid for documentation purposes as per [RFC 2606](http://www.faqs.org/rfcs/rfc2606.html), also I won't repeat the domain in all the other hostnames  
* sno-devl-mail, sno-devl-mailout, sno-stag-mail, sno-stag-mailout, sno-prod-mail, sno-prod-mailout \- I'll also leave out the hostnames for staging and production environments now. I'm pretty sure you are able to construct them yourself  
* sno-devl-storage  
* sno-devl-db  
* sno-devl-staticweb  
* sno-devl-appweb

A few points might need explanation.

**Why isn't the source code reposity a production service?**

Well it is, but since there's only one (and only one) we dump the environment. This is our convention for all SCM instances, it is well known so it's not a problem

**Why the "*appweb*" and "*staticweb*"?**

Those might sound:

* too complicated and  
* too generic

I think neither is true, we are sysadmins and don't really care wether it's a java application, PHP, Python, Rails or plain Assembler. What I need to now is where the application is so that I can directly go to a host that needs some reconfiguration in case it's necessary. The web part of the name is a hint that it's...well a web application. Yes in this day and age there are still some applications running on a server that don't provide a GUI on port 80\!

There are few other things we try to adhere too, while it may seem like quite a rule set that people need to keep in mind it's actually not that bad. People \- that is system administrators, developers *and end users* \- know about this scheme and can easily construct hostnames with little guessing. It's not too hard to write. I thought about moving from "*devl*" to "*devel*" but it's

* not worth the effort  
* everybody's already used to it  
* one more character to type

so I have enough excuses to purposely have a typo in there. But since we are dealing with artifical names anyway we don't have much of a problem here. We get very few questions about where a service actually is, and most questions are only asked once. Those come up when we obviously did something wrong abbreviating the usage but that is something we live with for the sake of not generating sources of error. Renaming a host is quite a risky thing to do, there are references all over the place you might forget and tests don't always cover all cases. We are hit early enough with missing test cases everytime we have to migrate some server or service due to scaling issues.

/2009-06-15
