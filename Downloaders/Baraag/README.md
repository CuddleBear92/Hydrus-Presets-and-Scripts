[See the help files for how to add downloaders to Hydrus](https://hydrusnetwork.github.io/hydrus/help/adding_new_downloaders.html)

This downloader pulls images at their original size directly from Baraag. If
you've muted a status (or "toot") through mastodon/Baraag's web UI, any images
from that status will be excluded from the results returned to Hydrus.

You might get away with running this without cookies / logging in but it's
likely you'll get rate limited unless you import your session cookies to Hydrus.
Even if you're properly authenticated, it's likely Baraag will still rate limit
you after a while. Hydrus _should_ handle this smoothly and back off when rate
limited.

Future work:

In theory, Hydrus's veto ability should support some simple form of client-side
filtering, allowing us to exclude any statuses we've filtered out of our feeds,
though I haven't explored this yet.
