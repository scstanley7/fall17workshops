# Webscraping with Python

Sarah Stanley<br/>
Digital Humanities Librarian<br/>
[scstanley@fsu.edu](mailto:scstanley@fsu.edu)

*With apologies and great thanks to Brandon Walsh and Ethan Reed, whose Humanities Programming curriculum and slides I have adapted for this workshop*

## Why Use Webscraping

* Automatically download large amounts of text and data from online resources
  * Text resources
  * Databases
  * but...
  
## Some caveats

It's important to check the terms of service for the site you want to scrape from!!

* Lots of requests to the site can make it run slower for everyone else
  * See the Project Gutenberg [terms of service](https://www.gutenberg.org/wiki/Gutenberg:Terms_of_Use#Audience) for an example
* Some people have restrictive data policies

It's best to ask if you don't know whether a site is ok with webscraping. Sometimes if you email the site owner, they may just send you the data you're looking for!

## Using Python for Webscraping

When you open a link in your browser, you are basically viewing HTML that has been styled and displayed by your browser. To look under the hood at the underlying HTML, use a browser like Firefox or Google Chrome, right click on the page and select "view page source."

When we download files or bits of HTML during this workshop, we will be interacting with that source HTML.

## HTML and CSS

In order to best utilize Python for webscraping, you need to have a basic understanding of HTML, so let's look under the hood at some raw HTML.

Let's go to https://lib.fsu.edu/drs to take a look at the source underneath.

## CSS selectors

CSS selectors are used in order to do specific styling on a page, by either selecting specific subgroups of content (using the `@class` attribute) or specific, individual elements (using `@id`). 

In CSS, you select: 

* a class by writing a period followed by the class name: `.classname`
* an id by writing a sharp sign followed by the unique identifier: `#identifier`

## More ways of finding elements with CSS selectors

* `elementName anotherElement` (with a space between the two element names) finds `<anotherElement>` *only* when it occurs within `<elementName>` (when `<elementName>` is an *ancestor* of `<anotherElement>`)
* `elementName > anotherElement` finds all of the instances of `<anotherElement>` whose *parent* is `<elementName>`

## Why do we care about selecting specific content?

* Find links on an index page to the *actual* content you are looking for 
* Remove contextual cruft from pages you're scraping from 

## Try selecting some content 

1. Find all the 3rd level headings
2. Find all the links inside four-column tables
3. Find a paragraph inside the element with the id of "section-footer"

## Answers

1. `h3`
2. `.four-column-table a`
3. `footer#section-footer p`

## Getting set up

* You'll need an account with DHBox: http://dhbox.org
  * Make sure you're using Google Chrome or Firefox!
* Follow along and find resources for today's workshop at https://github.com/scstanley7/fall17workshops/python-webscraping

## Modules for today

Today we'll be using a few modules:
* BeautifulSoup 
* contextlib
* urllib

## Calling in modules 

Usually, if we wanted to use different modules in Python, we would need to download and install them. You will need to do this if you are working on your own computers. But since DHBox has all the modules we'll need installed, we can just import the modules as we need them. The way that we do this is by writing:

`from [moduleName] import [functionName]`

So for our purposes, we'll need:

```
from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request
```

These modules will help us read, organize, and interpret urls and html content.

## Finding links 

Go to https://github.com/scstanley7/fall17workshops/tree/master/python-webscraping/html

At this address, you will a list of links to the Oxford Text Archive. Specifically, you will see links to six texts from the Early English Books Online - Text Creation Partnership initiative that have been transformed from TEI into HTML.

Right click on the page and select "view page source." This will show you the raw HTML for the page. You should see a lot of extra script and style information that is not present in the raw markdown README file (this is page source material that determines how GitHub is organized and displayed). 

We are going to want to find `<div>` element with an `id` of `README`.

## Open URLS 

```
readme_URL = "https://github.com/scstanley7/fall17workshops/tree/master/python-webscraping/html"
html = request.urlopen(readme_URL).read()
soup = BeautifulSoup(html, 'lxml')
ota_links = soup.select("ul#ota-links a")
print(ota_links)
```

## Get the GitHub URLs  

```
readme_URL = "https://github.com/scstanley7/fall17workshops/tree/master/python-webscraping/html"
html = request.urlopen(readme_URL).read()
soup = BeautifulSoup(html, 'lxml')
ws_links = soup.select("ul#ws-links a")

ws_urls = []
for link in ota_links:
  ws_url = link['href']
  ws_urls.append(ws_url)
  
print(ws_urls)
```

## Print some lines from the text

```
texts = []
for ws_url in ws_urls:
    print(url)
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    text = soup.text[0:1000]
    texts.append(text)
# print out the contents of the thing
print(corpus_texts)
```














