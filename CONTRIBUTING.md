# Contributing
## Pull request
Make a parser/downloader, if you don't know how see the Hydrucs help docs [here](https://hydrusnetwork.github.io/hydrus/help/downloader_intro.html). After that is done make a pull request, see the Github help docs [here](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request
).

Single-object downloaders should currently go into the /Downloaders directory. If there needs to be multiple objects or it needs a README for more in-depth usage instructions, create a folder named after the site (example: `Pixiv` or `Danbooru`).

## Naming
Name the exported downloader after the site, if it has some specific function not covered by default downloaders specify that, and the date of creation. Name in this case is both the filename and the title, you can specify both when exporting the downloader.  
An example is `pixiv bookmarks - 2020-11-23`. There is already a Pixiv downloader in Hydrus, this one is for downloading a user's bookmarked files instead of the normal tag search so you have site=pixiv, function=bookmarks, and date=2020-11-23.

For date formatting [ISO 8601 calendar dates](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates) is what we use. It makes it easy to see if a downloader is old and might need to be replaced and sorts properly if for some reason multiples of the same parser is present.

## Description
In the description field you can put a small blurb about specific requirements for the downloader to function. Example: `Needs site cookies to work.` or `Requires the pixiv default components hydrus ships with`.

## README
For readmes to display properly on the Github site they should be named `README.md`. First line should contain the following line:
```
[See the help files for how to add downloaders to Hydrus](https://hydrusnetwork.github.io/hydrus/help/adding_new_downloaders.html)
```