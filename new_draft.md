#Tools For Social Justice in Python

__By__

__Eric__ __Schles__

##Introduction

The goal of this text is simple.  To show you examples of tools that I've built to make the world a better place.  These tools incorporate much of the standard techniques computer scientists use.  So I won't be showing you anything you can't find in a blog post or in another great book.  But what I will be showing you is the mindset that I've come up with.  That's all software development is - taking logic and turning it into something a computer can do instead.  During this report I'll be showing you the tools I've made to fight slavery.  

Slavery is possibly the most important challenge of the current century, partially because solving it means solving all or many of it's contributing factors.  It's come out of a perfect storm of problems.  Some of these problems are easy to indentify and some of them are still unknown to us.  While many of them can be lessened with computers, this can only be a component towards finding a solution.  It's going to take people actually working together, not out of self interest, but out of a desire to make the world a better place, if we are going to solve these problems.  

Before we can understand how I've built the systems I've built, we must understand why.  That is to say, we must understand what problem I'm solving.  We'll begin by understanding modern slavery here in America and around the world.  Once we have the problem domain set up, we'll work through solutions that I've come up with.  These solutions cover a broad swath of computer science techniques.  I assume you will already know how to do each and that the only new piece of information is the combination of these tools and techniques.  

##Understanding Slavery

Slavery is a deeply complex issue, but it comes, in general, from one thing - income inequality.  The more disparity there is between people the great the possability of slavery occurring.  Because in general, slavery only affects the poor.  Of course, there are specific cases where people get kidnapped and that sucks, but the chances of becoming a slavery are far, far higher if you are poor.  And so to solve slavery, we must turning back the tides of income inequality, it is the only way.  Of course, this is just my opinion.  

Income inequality may only be a symptom of the problem and not the root cause.  Another possible root cause could be the internet.  With the availability of information, it is cheap to advertise anything.  And because of it's distributed nature, it's hard to control information on the internet.  Therefore it is relatively easier than at anytime in history to buy and sell anything, including people.  And there is a very large market for free labor.  A third arguement could be made for a change in laws.  When welfare, social security, financing for public education, and other government services began to dry up, when we stopped investing in americans, that likely contributed to a decrease in a stabilized economy, because wealth became centralized.  By not redistributing wealth and launching into unbriddled captialism, we have failed the people who needed these services the most.  At the end of the day, all of these factors are to blame for a rise in human trafficking - if we truly need someone to blame, we need only look to the decisions of our past leaders, in part.  

But I don't believe that they intended this as a consequence.  If we really need to blame anyone, there is really only two groups at fault, the traffickers and those who enable the traffickers.  The people who believe it is okay to enslave another person or believe it is okay to profit from these traffickers.  These groups are powerful, distributed, well resourced with lots of money, and international, with no or little central leadership.  Because slavery is a practice, a set of ideas, much like computer science.  You cannot claim any one computer scientist is responsible for computer science as a whole, but in our own way, we are all responsible for bits and pieces of computer science.  And we all share tools, techniques, skills, and experience with one another.  This is how slavery persists in the modern day.  And it must end.

So, now that I've spoke in broad strokes about our problem and the people who are causing this problem to happen.  It's time for the part I hate.  We are going to talk about how someone becomes a sex slave.  Every time I talk about this, my skin crawls, so get ready to feel disgusted, angry, sad, and maybe even extremely apathetic.  Please no, I take no pleasure in this knowledge, nor in describing it to you or anyone.  Everytime I think about this stuff, a part of me dies.  But I want you to be ready for the horrible truth, as we peal back the layer of civilization and look at the horrible thing that happens, sometimes, to some people, who don't deserve such a horrible existence.  

In this text we'll only talk about sex slavery.  There is also labor trafficking, organ trafficking, and child sex trafficking.  I'll be discussing those in other texts.  Sex trafficking happens a few ways:

Case 1. A person is kidnapped and forced into sex slavery 

Case 2. A person is mentally/physcially violated to such an extreme place, they submit to the will of the trafficker

A possible solution to 1 - Match missing persons pictures with pictures from sex marketplace websites such as backpage

Solving 2 is harder.  To understand how to stop problem 2, we must understand the approach a trafficker uses to break his victims:

Case 2: Part A - The trafficker cuts off the victims social connections and emotional support center, refocusing this system souly on them ~ 3-7 months

Case 2: Part B - Once the victim has no other or a very small social/emotional support center, the trafficker begins to physically beat the victim or rape them ~ once per month

Case 2: Part C - Then the victim is moved into a small living quarters with other victims and made to compete for the traffickers attention and affection by making the trafficker money.  

Case 2: Part D - The trafficker reinforces a pattern of control with a combination of violence, rape, and occasionally consential sex. ~ beats or rapes them once per month.  Trafficker says the victim will be beat or raped nearly constantly.  At this point the victim is trapped. 

To make this concrete let's walk through a few scenarios of how a person might end up in the second case:

1. A teenager meets a much older person, either on the internet or in real life.  The teenager leaves their family to be with this older person after a period of time, typically 3-6 months.  Eventually the older person claims that the teenager needs to help out the older person, because they have financial trouble.  That the teen needs to sell their body for sex to help support the older person.  Sometimes the teen submits to this.  Other times they do not.  At the first sign of giving up or disobdiance, the older person becomes violent, abusive, and will likely rape the teenager or have someone else rape the teenager.  At this point, we can refer to them as a trafficker.  The trafficker will threaten to kill the young person.  This is known as breaking in, in the trafficking community.  Once the teen has been broken in, the trafficker will force the young person to sell their body for sex.  They trap the teenager in a prison of the mind, where the young person has no escape, no will of their own.  This induces a form of PTSD.  Suicide, depression, in ability to cope, are all likely side-effects of the continual threat of violence, rape, and possible murder.  

2. A gay teenager runs away from home.  Unable to deal with their family or thrown out of their house by their parents.  They may end up in a major city, like New York City.  There they may meet an older person by chance who is kind to them at first, buys them meals, gives them shelter.  After 3-4 months of generousity, the older person will ask the young person to work for them as a prostitute.  They will claim the teenager owes them money for all of their kindness, they will guilt them, and try any tactic to manipulate them.  The goal is singular, to control the teenager.  Should the teenager refuse, violence, rape, and the threat of murder will be brought to the young person.  At this point, the older person can be called what they are, a trafficker.  From here the story is the same as above.

There are more scenarios - people are brought to America to become models, but when they get here, they are forced into prostitution in a similar fashion.  Sometimes, young people are kidnapped.  

Out of all of these scenarios, there is one common thread - a poor and vulnerable person has their social network removed and then they are manipulated into prostitution, forced into a culture of rape.  

So this is how it happens, once a critical point has been reached - namely a young person is in a situation with very little money and a very small or nonexistant social support center.  Then all a trafficker needs to do is completely destroy that social support center and refocus it on himself.  

I wish this type of knowledge wasn't out there, but there are books written by traffickers on how exactly to traffick young people.  So sadly, this isn't secret or unknown information.  In fact, there are whole communities of traffickers, sharing techniques, growing, and evolving together.  This makes trafficking in America extremely hard to stop, and even harder to predict - because they are capable of learning and adapting as new challenges are created.  

Presently law enforcement attacks the problem by intervening when the victim is in Case 2, part D.  Sometimes we are able to intervene sooner, but usually we are not.  

I've built a system that automates much of the investigative work in cases 1 and 2.  We'll look at both of these systems in detail.  But what we really need is a system that understands the __contributing__ __factors__ that led to that person becoming a victim in the first place and understand the "basket" of policy choices they can employ to limit the amount of trafficking and to hit reasonable goals to reduce human trafficking supply.

The last system I will be covering is the one I am currently building.  It addresses this question - how do we build analyses that will aid the in combatting human trafficking, not just when a person has become a victim, but how do we stop them from becoming a victim?

##Understanding The Solutions

System 1 - FindMe - finding victims that were kidnapped

This system called FindMe compares pictures found on backpage.com and other commercial sex websites with pictures found on missing persons websites.  If a match is found an investigation is launched.  

This system leverages facial recognition, content based image retrieval, and image cleaning techniques

System 2 - Investa_gator - finding victims that were manipulated

This system automates the process of finding new victims of trafficking, given a set of victims.  This system leverages web scraping, document similarity, text cleaning, named entity recognition, link analysis, database design, and address processing techniques

System 3 - PolyWonk - does policy analysis and prediction to stop trafficking at the systemic level

This sytem leverages large data processing, time series analysis, time series visualization, GIS visualization, GIS prediction, impulse response, and potentially other techniques (since it's not finished yet).  

 