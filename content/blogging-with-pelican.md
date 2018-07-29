Title: Blogging with Pelican
Slug: blogging-with-pelican
Date: 2018-07-25 18:48:43
Category: Misc
Summary: How this blog is made
Tags: blog, pelican, python

The blog is made using [Pelican](https://blog.getpelican.com){:target="_blank"} and it's published using [GitHub Pages](https://pages.github.com){:target="_blank"}
To create the basic setup I mostly followed [this guide](https://fedoramagazine.org/make-github-pages-blog-with-pelican/){:target="_blank"}.

## Install Pelican
To install Pelican you just need to install *pelican* and *markdown* python modules:

	:::console
	$ pip install pelican markdown

You may need to use sudo, it depends on your setup.

If you check Pelican docs, you will see that they recomend to use virtualenv. I didn't feel it necessary, but if you want to use it, be my guess.

## Create a GitHub user page
GitHub allows to create *project pages* and one *user page*. *Project pages* are tied to a specific project while *user pages* are generic.

The first step is to create 2 new repositories in your GitHub account. You know the drill, or just go [here](https://github.com/new){:target="_blank"}  
Both of the repositories must be *Public* and initialized with a README file.  
The first repository must be named *username.github.io*. Replace *username* with your username in GitHub. In my case, as my user is *Elhodred*, the repository is named *Elhodred.github.io*. This repository will contain the static site Pelican generates.  
The second repository can be named as you want, but my recomendation is to name it *username.github.io-src*. In my case, it becomes *Elhodred.github.io-src*. This way we identity directly this repository for what it really is: the repository that holds the sources of the blog.

## Setup the basic blog
Let's clone the source repository:

	:::console
	$ git clone https://github.com/Elhodred/Elhodred.github.io-src.git
	$ cd Elhodred.github.io-src/

Remember to replace the URL with the one for your repository.

Now we will add the repository that will hold the site as a submodule:

	:::console
	$ git submodule add https://github.com/Elhodred/Elhodred.github.io.git output

At this point, we can create our site:

	:::console
	$ pelican-quickstart
	> Where do you want to create your new web site? [.]
	> What will be the title of this web site? Elhodred\'s Notebook
	> Who will be the author of this web site? Alfonso Pinto
	> What will be the default language of this web site? [en]
	> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) y
	> What is your URL prefix? (see above example; no trailing slash) https://elhodred.github.io
	> Do you want to enable article pagination? (Y/n)
	> How many articles per page do you want? [10]
	> What is your time zone? [Europe/Paris] Europe/Madrid
	> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
	> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
	> Do you want to upload your website using FTP? (y/N)
	> Do you want to upload your website using SSH? (y/N)
	> Do you want to upload your website using Dropbox? (y/N)
	> Do you want to upload your website using S3? (y/N)
	> Do you want to upload your website using Rackspace Cloud Files? (y/N)
	> Do you want to upload your website using GitHub Pages? (y/N) Y
	> Is this your personal page (username.github.io)? (y/N) Y
	Error: [Errno 17] File exists: '/Users/elhodred/code/Elhodred.github.io-src/output'
	Done. Your new project is available at /Users/elhodred/code/Elhodred.github.io-src

Don't worry about the error, it's normal as we already created the output directory.  
We just need to edit *publishconf.py* file and set *DELETE_OUTPUT_DIRECTORY* variable to *False*. This will prevent Pelican deleting the output directory each time you publish the site.

## Makefile improvements
Pelican doesn't include a command to create new articles or pages. But that's very easy to fix. Edit the *Makefile* and add the following before *.PHONY*

	:::make
	newpost:
	ifdef NAME
		echo "Title: $(NAME)" >  $(INPUTDIR)/$(SLUG).$(EXT)
		echo "Slug: $(SLUG)" >> $(INPUTDIR)/$(SLUG).$(EXT)
		echo "Date: $(DATE)" >> $(INPUTDIR)/$(SLUG).$(EXT)
		echo ""              >> $(INPUTDIR)/$(SLUG).$(EXT)
		echo ""              >> $(INPUTDIR)/$(SLUG).$(EXT)
		${EDITOR} ${INPUTDIR}/${SLUG}.${EXT}
	else
		@echo 'Variable NAME is not defined.'
		@echo 'Do make newpost NAME='"'"'Post Name'"'"
	endif

	editpost:
	ifdef NAME
		${EDITOR} ${INPUTDIR}/${SLUG}.${EXT}
	else
		@echo 'Variable NAME is not defined.'
		@echo 'Do make editpost NAME='"'"'Post Name'"'"
	endif

	newpage:
	ifdef NAME
		echo "Title: $(NAME)" >  $(PAGESDIR)/$(SLUG).$(EXT)
		echo "Slug: $(SLUG)" >> $(PAGESDIR)/$(SLUG).$(EXT)
		echo ""              >> $(PAGESDIR)/$(SLUG).$(EXT)
		echo ""              >> $(PAGESDIR)/$(SLUG).$(EXT)
		${EDITOR} ${PAGESDIR}/${SLUG}.$(EXT)
	else
		@echo 'Variable NAME is not defined.'
		@echo 'Do make newpage NAME='"'"'Page Name'"'"
	endif

	editpage:
	ifdef NAME
		${EDITOR} ${PAGESDIR}/${SLUG}.$(EXT)
	else
		@echo 'Variable NAME is not defined.'
		@echo 'Do make editpage NAME='"'"'Page Name'"'"
	endif

And then modify .PHONY adding this at the end:

	:::text
	newpost editpost newpage editpage

Those are the new commands available using make. They allow you to create/edit articles(posts) and pages.

To create a new post:

	:::console
	$ make newpost NAME='The title for the post'

## Replacing the theme
Here you can find several themes for Pelican. In my case, as I want only one theme, I did the following.

First, I chose [Pure](https://github.com/PurePelicanTheme/pure/){:target="_blank"} as my theme. Then I forked it and added it as a submodule in my sources repository:

	:::console
	$ mkdir themes
	$ git submodule add https://github.com/Elhodred/pure.git themes/pure

This allows me to make my own changes to the theme while I can keep in sync the changes made by the original author.

Finally, edit *pelicanconf.py* and add the following:

	:::python3
	THEME = "themes/pure"

## Testing your site
There are a few configuration options you can add to *pelicanconf.py*. Between them you will find the following ones:

	:::python3
	COVER_IMG_URL = "/images/sidebar.png"
	PROFILE_IMAGE_URL = "/images/profile.jpg"
	TAGLINE = "A Developer's journey"

*COVER_IMG_URL* is the URL for the image to use on the left side of the page when listing posts.  
*PROFILE_IMAGE_URL* is the image of the author of a post. Is the circle avatar shown on the left side of the page when a post is rendered. In the official Pure them it doesn't work despite what it says in the documentation as they use gravatar. I didn't want to use gravatar so I modified my fork to use again this variable.  
*TAGLINE* is a text that appears below the blog title on the left side of the page.

To let Pelican copy the images as static content, first create a directory called images under content folder:

	:::console
	$ mkdir content/images

And then let *Pelican* know that it has to use that folder for static content. Add this to *pelicanconf.py*:

	:::python3
	STATIC_PATHS = ['images']

Put the images you want to use in the images folder and update the *COVER_IMG_URL* and *PROFILE_IMAGE_URL* to match the names of your files.

## Tweaking URL schema
If you want to have a better looking URL in the form *http://domain/postname* and, according to some SEO recomendations, better for the search engines, you can use the put the following in *pelicanconf.py*:

	:::python3
	ARTICLE_URL = '{slug}/'
	ARTICLE_SAVE_AS = '{slug}/index.html'
	PAGE_URL = '{slug}/'
	PAGE_SAVE_AS = '{slug}/index.html'

## Publish your site
First, we need to regenerate the site with *production* settings:

	:::console
	$ make publish

Then, go to the *output* directory and commit and push as usual:

	:::console
	$ cd output
	$ git add .
	$ git commit -m 'First post'
	$ git push origin master

Congratulations, your site should be online.
