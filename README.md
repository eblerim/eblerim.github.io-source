# source for http://eblerim.github.io

This repository contains the source for my Pelican powered blog served through GitHub pages http://eblerim.github.io

The template of my blog it's based on Jake VanderPlas [Pythonic Perambulations blog](http://jakevdp.github.io) (MIT license), which was adapted from Daniel Rodriguez [blog](https://github.com/danielfrg/danielfrg.github.io-source) intially released under the Apache v2.0 license. Otherwise, prerequisite to understand the inner workings of this  repository is to have experience (at least) with Git, GitHub, GitHub Pages, ghp-import (needed to import effortlessly GitHub Pages), shell commands, Makefile and Python. Some motivation for choosing Pelican for static blogging and coming up with this particular solution I have provided in this blog [post](http://eblerim.github.io/blog/2018/10/31/githubpages-pelican-opensource/).


## Building the Blog

Clone the repository & make sure submodules are included

```
$ git clone https://github.com/eblerim/eblerim.github.io-source.git
$ git submodule update --init --recursive
```

Install the required packages:

```
$ conda create -n pelican-blog python=3.5 jupyter notebook
$ source activate pelican-blog
$ pip install pelican Markdown ghp-import
```

Build the html and serve locally:

```
$ make html
$ make serve
$ open http://localhost:8000
```

Deploy to github pages

```
$ make publish-to-github
```

If you plan to use this tempalte for your own blog then don't forget to change the `GITHUB_PAGES_REMOTE` variable in the `Makefile`. Moreover, note that the Makefile is configured to work for a GitHub User Page and not a GitHub Project Page, for more information [see](https://help.github.com/articles/user-organization-and-project-pages/). Otherwise, make sure to copy the hidden files (.gitignore and .gitmodules) into your directory, which are commonly refered to as dotfiles.