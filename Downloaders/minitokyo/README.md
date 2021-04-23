How to use:
Get numerical tag id you want to download by going to minitokyo, search for the thing you need, then go to any category and check URL for tid parameter.
Copy the numerical tid parameter, and use it to perform search with any minitokyo GUG.

Why?

First, let's see how minitokyo works. There are 3 different post categories:
- wallpapers - usually made from other works with some filters, scaled/cropped to common resolutions
- indy art - unsorted fanworks
- scans - the meat of minitokyo, high-resolution scans of official and unofficial albums.

When searching for a human-readable tag (such as "Touhou"), minitokyo returns description page for the tag, from which one of the three categories can be looked through. When browsing any category, you might notice that your tag disappears from the URL and turns into a tag id (such as tid=1262). Since human-readable tags are only used to look up tag description, actual search is performed with tag ids, and there is no obvious table for simple conversion of a tag to its corresponding id.

Due to the way hydrus downloaders work, it's not that simple to query with a human readable tag, turn it into tag id, then continue the query with the category selector. Which is why it works this way.