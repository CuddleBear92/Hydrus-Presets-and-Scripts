# The Download System
The NEW Download System
It Encompasses Parsers, URL Classes, GUG's, nGUG's and Simple Downloaders

URL Classes tells the client what the URL is and is linked directly to a Parser that will look at the URL in question for info and links.
GUGs can generate URLs that the URL Class understands out of an example of the URL and a replace key for the query/search.
nGUG's group GUG's together so they do the same query/search across many GUG's at once.
Parsers look at the URL for links and info to pull as files and tags, Parsers can also give an URL to the URL Classes that will give it to another Parser so Parsers work together.

## Example on a query with a GUG works
GUG's or nGUG's (which gives it to a GUG) takes the user query/search and makes an URL out of it.
The URL Classes will look at this URL and compare it if it matches any URL Class.
It will then try to hand this URL to the Parser linked in the URL Class Links.
The Parser will get this at this point and try to Download the post or gallery. 
With Galleries it will grab all thumbnail URLs and the next page URL and hand that over to the URL Classes again.
Posts will be handled by the URL Classes and sent to its own Post Parser which grabs the file and tags.
The next page URL will also be handled by the URL Classes again and sent back to the same gallery Parser to repeat its step for more thumbnail links.