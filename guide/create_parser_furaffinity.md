# Guide how to create parser for Furaffinity

This guide is create on Hydrus version 315

post url: https://www.furaffinity.net/view/28048695/

## Create Url class

Before creating url class you have to understand how url work and parts of it.

see url for complete explanation: https://en.wikipedia.org/wiki/URL

tldr: url path components is part of the folder tree of the sites.
A site is a folder and file structure in most cases after all.

Parameters section will handle url query. 
In this case it will be removed because post url dont' contain any query
string.

Url class tells the client how an url looks like and what type of url it is

There is categories you put them in.
In classes like a post class which would be a post url.
That will then be linked together with a parser that will look at the url in
question and parse that info on how it will be processed.

![](/guide/fa_1.png)

*`downloaders definition` menu*

- open `network` menu > `downloader definition` menu > `manage url class menu`
- click `add` button
- add proper name e.g. `furaffinity post`
- add the url you want to match to example url
- set `url type` as `post url` because we will get image url from this
- set `network location` to match the example url (`www.furaffinity.net`)
- set path to match the url
- clear item on `parameters` section

![](/guide/fa_3.png)

*items on parameters section which have to be removed*

![](/guide/fa_2.png)

*complete result*

Note:

some urls can be normalized down and shortened to remove things that isn't needed like this:

![](/guide/fa_4.png)

*normalized and shortened url*

further reference http://hydrusnetwork.github.io/hydrus/help/downloader_url_classes.html

## Create Parser

![](/guide/fa_1.png)

*`downloaders definition` menu*

- open `network` menu > `downloader definition` menu > `manage parsers`
- click `add` button
- set a name for it e.g. `furaffinity post parser`
- place the post url in the example urls on the left
- paste in the post url in the fetch test data field.
it will just get the html code for that url as is
- click `fetch test data from url` button on the right
- grab the file
  - open your post page on the browser
  - right click to inspect the download url
  it will give you something like this
  ```html
  <a href="//d.facdn.net/art/hypoempathy/1532040044/1532040044.hypoempathy_dekukun.png">Download</a>
  ```
  - add a new content parser 
  - name it `url file`
  - edit formula at the bottom of that window and get it to find that `href` for you.
  its pre applied with an `<a>` tag and fetches the content of the attribute `href`
  - you can double click that `<a>` tag line to edit it
  - edit the tag string match under the `a` tag so the tag string matches `Download`
  - test parser in the formula window. The results should give the url
  - press `apply` to go back to the content parsers on the main window

  ![](/guide/fa_5.png)

  *`a` tag parser*
- parse the metadata and tags to parse by adding another content parser. Its done the same way.

namespace must not be unclassified. It is depend on sites.
you can right click and inspect the keywords in your browser to gain the general tags.

![](/guide/fa_6.png)

*final result for getting file url*

![](/guide/fa_7.png)

*getting keywords tags*

![](/guide/fa_8.png)

*getting creator name*

![](/guide/fa_9.png)

*getting title*

## Link Url class with Parser

- open url class link
- double click on post url entry
- select the parser
- press `apply` button

![](/guide/fa_10.png)
*linked post url and post parser*
