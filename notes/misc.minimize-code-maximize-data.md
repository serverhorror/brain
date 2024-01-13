---
id: zw8jd9fp6e6xeereqa0d02i
title: Minimize Code Maximize Data (database-programmer.blogspot.com)
desc: ''
updated: 1705153321511
created: 1705153001992
---

* Source:
  * [Minimize Code, Maximize Data (database-programmer.blogspot.com)](https://database-programmer.blogspot.com/2008/05/minimize-code-maximize-data.html)

> Sunday, May 4, 2008
> 
> ### Minimize Code, Maximize Data
> 
> Early in my career, I was fortunate to receive some programming lessons from one of the early pioneers in computer age, [A. Neil Pappalardo](https://en.wikipedia.org/wiki/Neil_Pappalardo). While I am sure he would not remember me, I certainly remembered him, and he said one thing that I remember very much: Minimize Code, Maximize Data.
> 
> This is the Database Programmer blog, for anybody who wants practical advice on database use.
> 
> There are links to other essays at the [bottom of this post](#bottom).
> 
> This blog has two tables of contents, the [Topical Table of Contents](https://database-programmer.blogspot.com/2008/09/comprehensive-table-of-contents.html) and the list of [Database Skills](https://database-programmer.blogspot.com/2010/11/database-skills.html).
> 
> ## The Best Kept Secret in Programming
> 
> This week we are going to examine what I was told so many years ago:
> 
>> Minimize Code, Maximize Data
> 
> Since then, and it was nearly 15 years ago, I have never once heard another programmer (except myself) express this very basic and simple idea. It is the best kept secret in programming. I can think of two reasons why most programmers working today have never heard the simple idea, "minimize code, maximize data."
> 
> First possibility: the guy was totally wrong. I highly doubt this however as his company is approaching its 40th year of worldwide growth, and how many companies in this field last that long, never mind prosper and grow?
> 
> The second possibility seems much more likely to me: most programmers just don't think that way. Most programmers would never stumble upon this idea on their own and if they do hear it they forget it or reject it. We programmers love to code, and are reluctant at best to accept the idea that he who codes least codes best.
> 
> Now we will see how this simple idea impacts the entire software cycle, from designer to user.
> 
> ## The Example: Magazine Regulation
> 
> Our example is fairly easy. Consider a magazine distributor, a company that receives magazines in bulk and distributes them to stores. His system contains a table called DEFAULTS that lists the default quantity of each individual magazine that is distributed to each store (a big fat cross-reference table).
> 
> Now for the tricky part. Let's say we run a "SELECT SUM(qty)" from the DEFAULTS table for TV GUIDE and we get 2123. That means he needs 2123 copies of TV GUIDE to give every store their default delivery. But when the magazines arrived from the supplier, they only received 1900. What does he do? Well it so happens this happens every day, the distributor in fact _never_ receives his exact default requirements, they are always over or under. So the distributor must run a process called _regulation_.
> 
> Regulation is an automatic computer process that runs through the defaults, compares them to what you actually have, and increases or decreases the delivery amounts to each store until everything lines up. It is by nature iterative, you run through the stores over and over increasing amounts by one or two until you balance out. Next we will look at how to write it.
> 
> ## Writing a Regulation Program
> 
> Before we get to the details of the regulation program, I have to point out one detail about magazine distribution. It turns out that 50-80% of magazines sent to retail racks go back to the distributors and are shredded. This means it is not uncommon to talk about sales percentages of 50% or 60%. If a store is receiving too many magazines, they might easily have a sales percent as low as 10%.
> 
> So how do we write the regulation program? I'm going to avoid any long build-up here and just go straight to the answer. You make a table of rules that determine how the regulation process works. The owner of the distribution company will say things like, "If the store sold less than 20% of the TV GUIDES for the past 4 weeks, drop their amount by 2, but do not go below 2." So you make a table with columns like "THRESHOLD\_PERCENT", "DECREMENT" and "ABSOLUTE\_MINIMUM". There will also be rules that operate when the company has too many magazines. The owner says, "If his sales percent is greater than 80%, give him two more." So your table now contains percentages and increase amounts to use when raising the distribution amounts.
> 
> From here your program is reduced to a fairly simple affair, it is little more than a double-nested loop. You fetch a list of the rules, in order, and you begin to iterate through the magazines, applying the current rule to the current magazine. You keep applying each rule over and over until there are no more cases where it applies, then you move on to the next rule. As soon as the total magazines matches the amount you have, the program terminates. It is the very soul of simplicity, and a perfect example of what database applications can do so well.
> 
> ## The Wrong Way To Do It
> 
> It so happens that I have a customer who is a magazine distributor, which is how I learned about this process. The system he is using now, which I maintain for him, was not written as I described it above. There is no table of rules. The programmer coded up each different rule separately, and the programmer is now dead (I feel like Dave Barry saying this, but I swear I am not making this up). The owner and I are both afraid to touch the code, and so he lives with it while we plan for something better.
> 
> While I do not wish to speak ill of the deceased, it is safe to say that the original programmer did not know he was supposed to minimize code and maximize data. Let's examine the consequences of that ignorance:
> 
>> The customer is not in total control of his own business, because he  
> cannot reliably modify one of his most basic operations.
> 
> So we can now draw the conclusion that the "minimize code, maximize data" has very direct consequences for the user experience, especially those very important users who sign the checks.
> 
>> The Impact Upon Your Code
> 
> A code grinder who is not trying to minimize code usually ends up with very complicated programs. This is true even of veteran and expert programmers who supposedly know better. They set out with an idea to simplify things and then end up writing complex heavily inter-dependent class libraries. I contend that this happens because they don't know that they are supposed to minimize code by maximizing data.
> 
> On the other hand, the database programmer who knows to maximize data ends up with dramatically simpler code patterns. This happens because a lot of the complex conditionals and branching logic that is required for code-centric solutions is reduced to row scanning operations that contain much simpler algorithms in the innermost loop.
> 
> We can see this in the example above for the regulation program. The data-centric solution is basically one loop nested inside of another with the core operation occurring on the inside. The code-centric solution, which I mentioned we are afraid to touch, is full of conditionals and branches that make it dangerous to mess with for fear of causing unintended side-effects. The original programmer could probably do anything with it, everybody else is reduced to doing nothing.
> 
> The problem becomes more exaggerated as time goes on. As programs mature, their original simplicity is enhanced to handle more sophisticated edge cases and exceptions. As this process continues, many of these sophisticated edge cases and exceptions will be mutually exclusive or will interact in subtle ways. When this happens the code-centric program becomes increasingly difficult to understand and keep correct, as the layering of conditionals and branches and interdependencies makes it harder and harder to eliminate unwanted side effects. The data-centric solution on the other hand, while still becoming more difficult, is reduced to simply making sure that the tables provide the correct options for the code, and the code remains a matter of scanning the rules, picking precedence, and executing them.
> 
> ## The Impact on Debugging
> 
> It is much easier to debug data than code, especially when a simple operation has been matured to handle a collection of subtle edge cases and exceptions that may interact with each other.
> 
> If we continue to the example of the regulation process, the basic question arises, how do you test this thing? The entire concept of reliable testing is far more than we can cover in a single essay, but I do want to introduce the idea of testing with -- you guessed it, more data.
> 
> The regulation program as I have described it loops through rules and magazine quantities and adjusts those quantities. It is a row-by-row process, with each pass through the inner loop executing a single change. Debugging this process can be vastly simplified if a table is made that records, in order, each update that was made and what rule was used to make the update. Obvious errors could be detected if a rule was being applied out of order, or if the rule made the wrong change. Generating the test cases brings in yet again more data, creating a body of magazines, defaults and customers that deliberately stresses the system with extreme cases.
> 
> This debug-the-data approach can have a huge impact on boosting the customer's confidence and control. If he can directly view this log he has a perfect black-and-white explanation of how the process ran. If he does not like it he can change the rules. If you let your program run in "planning only" mode, where it generates these logs without making the changes, then your customer can play what-if and you will find you have truly made a new friend!
> 
> ## Meta-Data and the Data Dictionary
> 
> This week's essay leads naturally to the matter of meta-data and data dictionaries and how they can dramatically reduce the amount of code needed for routine table maintenance tasks. However, that is a large topic and must be reserved for one or more future essays.
> 
> When we get to the topic of data dictionaries, we will be looking at how a data dictionary can give you true zero-code generated table maintenance forms, among other things.
> 
> ## Conclusion
> 
> The motto "Minimize Code, Maximize Data" is not well known in popular discussions today, which I contend is a natural consequence of our basic personalities as programmers. Coding is what we do and we tend to think of solving problems as an exercise in code and more code.
> 
> Nevertheless, we have seen this week in a specific example (which could be repeated many times over) that the code-centric versus data-centric decision impacts everybody. The rule "Minimize Code, Maximize Data" has positive impacts and the coding process, the debugging process, the maintenance process, and the user experience. Since that covers all parties concerned with software development, it is safe to conclude that this is a crucial design concept.
> 
> ## Related Essays
> 
> This blog has two tables of contents, the [Topical Table of Contents](https://database-programmer.blogspot.com/2008/09/comprehensive-table-of-contents.html) and the list of [Database Skills](https://database-programmer.blogspot.com/2010/11/database-skills.html).
> 
> Other philosophy essays are:
> 
> *   [Prepare Now For Possible Future Head Transplant](https://database-programmer.blogspot.com/2010/11/prepare-now-for-possible-future-head.html)
> *   [The Quest for The Absolute](https://database-programmer.blogspot.com/2008/09/quest-for-absolute.html)
> *   [I Am But A Humble Filing Clerk](https://database-programmer.blogspot.com/2009/03/i-am-but-humble-filing-clerk.html)
> *   [Why I Do Not Use ORM](https://database-programmer.blogspot.com/2008/06/why-i-do-not-use-orm.html)
> *   _[Minimize Code, Maximize Data (this essay)](https://database-programmer.blogspot.com/2008/05/minimize-code-maximize-data.html)_
> 
