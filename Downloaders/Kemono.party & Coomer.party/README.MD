[See the help files for how to add downloaders to Hydrus](https://hydrusnetwork.github.io/hydrus/help/adding_new_downloaders.html)

## Kemono.party Downloader

Currently supports Patreon, Fanbox, Subscribestar and Gumroad content.

Separate GuGs are used for each site.

The site still occasionally gives errors, so be prepared to check for that stuff.

## If you're recieving 403 errors

Kemono.party has recently added DDoS-Guard protection, which can prevent Hydrus from accessing the site. Using cookies from a browser can work around this issue. Cookies can easily be sent to Hydrus using [Hydrus Companion](https://gitgud.io/prkc/hydrus-companion).

## Notes

If you imported this downloader before January 25th, 2021, delete k.p parsers and url classes with "gr/ss" in the name.

The parser uses the time a post was added to Kemono.party as source time by default. If you would rather use the date a post was published on the source site, follow these instructions:

1. Open "kemono.party userpage api parser"
2. Open the "posts" subsidiary page parser
3. Open the parser "added time"
4. In the parser formula, replace the word "added" with "published"

Keep in mind, however, that source time is used for subscription checking timing, and making this change could throw off automatic timing.
