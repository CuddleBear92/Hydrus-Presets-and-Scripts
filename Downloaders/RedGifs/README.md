You will need to import the **Authorization** and **User-Agent** header from your browser into hydrus.

The best way to do that is to *inspect* the search page and look in the *newtork-tab* for a request that starts with *search?order=* after you searched for something.

And then go *network* -> *data* -> *manage http headers* and insert them into the corresponding entries.
