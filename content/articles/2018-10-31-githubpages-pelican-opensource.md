title: GitHub Pages, Pelican and Open-source Software: Rapid prototyping and MVP
date: 2018-10-31 10:00
comments: true
slug: githubpages-pelican-opensource
tags: open-source software, rapid prototyping, pareto principle, python


## Introduction

For some time now, I have been interested to 're-lunch' my blog, which means I have never had an active blog but have kept one in a side—powered by WordPress and Twitter—since the times of my Ph.D. years (2009-2014). Mostly for the sake of having hands-on experience and not only relying on my theoretical insight and intuition as far as understanding blogging as a platform and supporting modern technologies. 

Perhaps, before I continue is good to mention that my experience with web development, on and off, dates back to 1998 by creating a simple homepage with the help of HTML 4.0, CSS and some Javascript. This experience, certainly got improved while I pursued B.Sc. in Computer Science (2003-2007) at university, during which I created and delivered some eCommerce websites by exploiting various web technologies of the time, such as ASP.NET, LAMP-stack, Macromedia (now Adobe) Flash, and so on. Nonetheless, I have never been interested to get deep into the web development (front-end or back-end) as such.


## Requirements for the blog 

To put the thing bluntly, my key requirement was to select a blogging framework made for hackers and useful to data scientists (embracing Python data science stack) that is simple yet powerful. Moreover, I also composed a short wish list. For example,

* I wanted the platform to be for static blogging (i.e., it doesn't require a database or server-side logic), Python-based and well-integrated with GitHub Pages;
* I wanted, as much as possible, to leave the source of my posts unmodified and preferably writing my posts in markdown (enabling me to make use of my skills and experience in writing documentation for various solutions and GitHub repos);
* I wanted easily and organically to be able to insert IPython notebooks into my posts;
* I wanted a platform that is open source, has an active community, makes available a wide array of themes and plugins, and the plugin and theming API to be well-documented and straightforward to use; and
* last but not least, I wanted to find a theme that is simple, clean and compact, and that includes some key aesthetics aspects that I believe a good blog has to have.


## Strategy and action plan

For more than 7 years now, I have been preaching and implementing the Pareto principle (aka 80/20 principle or minimum effective dose), rapid prototyping, and first delivering MVP and then MLP (i.e., first delivering Minimum Viable Product and then Minimum Loveable Product). It is perhaps needless to say that the same philosophy and set of principles underpins the strategy and action plan in addressing the above goal(s). Nonetheless, this time I got truly lucky and "the treasure(s) that I sought to find elsewhere I found at my doorstep". Actually, everything came to me as a gift from JakeVander Plas blog [Pythonic Perambulations](http://jakevdp.github.io), who, together with Wes McKinney, is a key Python-based Data Science author that has deeply influenced my data science work and understanding. 

Nonetheless, is worth mentioning that it took me few evenings' effort to understand hidden details of the embraced tech stack, especially things that related in correctly tracking and pushing things through Git and GitHub, and serving them through [GitHub Pages](http://github.io).


## Conclusion

I am already hearing some voices in my head that wonder if is this really good praxis? For example, is it alright to stand on the technical solution of others by importing their code? This is rather long and established topic in modern software development and data science, and without further ado I will leave you with two slides from Jake VanderPlan keynote talk at PyCon 2017, which is available through [YouTube](https://www.youtube.com/watch?v=ZyjCqQEUa8o). I believe, the quote from the first slide to be particularly known to researchers, especially those using Google Scholar J 

{% img /images/newton.jpg %}

{% img /images/not_newton.jpg %}

If you'd like to see the source from which this blog built and read the documentation, it's available on [GitHub](https://github.com/eblerim/eblerim.github.io-source). Feel free to adapt the configurations and theme to suit your own needs.

## What this blog post **is not** about
* What is the difference between GitHub User/Organization Page and GitHub Project Page? For that, [see](https://help.github.com/articles/user-organization-and-project-pages/).
* How to build a blog or site with GitHub Pages and Pelican? For that, [see](https://pythonforundergradengineers.com/how-i-built-this-site-1.html).
* How to migrate to GitHub Pages using Pelican from WordPress? For that, [see](http://mathamy.com/migrating-to-github-pages-using-pelican.html).
* How to migrate from Octopress to Pelican? Or, in order to get a deeper motivation and insight about embraced tech stack, [see](http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/).

*Happy learning and sharing!*