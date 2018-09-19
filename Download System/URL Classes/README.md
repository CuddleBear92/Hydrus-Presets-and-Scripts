# URL Classes
They are classes for URL's. They tell the client WHAT an URL is, if its a post, file, gallery, watcher (thread).
This will allow the client know how to handle them in different ways.
URL classes can also link with each other with the optional API filed. this can be used to point to the API version of the same URL or just hand it off to another URL class after transformation.
These only tells the client what the URL are, not how to download or handle them.

URL Classes will match automatically with GUG's and will try to match with example URLs in parsers with the `manage URL class links`

## How to Install URL Classes
You can import URL Classes under `Network>Downloader Definition>Manage URL Classes`


## Link an URL Class to a parser
Normally you can link URL Classes semi-automatically by going to `Network>Downloader Definition>Manage URL Class Links` and pressing `Try to Fill in Gaps Based on Example URLs`
This will try to match your UNLINKED URL Classes with examples saved in your Parsers.