[See the help files for how to add downloaders to Hydrus](https://hydrusnetwork.github.io/hydrus/help/adding_new_downloaders.html)

This downloader pulls images at their original size directly from Fanbox.
It supports URLs of the form `https://www.fanbox.cc/@username` as well as
`https://username.fanbox.cc`. Post summaries are added as notes.

## Authentication
You will need the following information to authenticate with, and be
authorized to use, the Fanbox API:

### Cookies
You must import your session cookies to Hydrus for this downloader to work.
*At the very least,* you must have `cf_clearance` and `FANBOXSESSID`. This
may be a moving target, so importing all your cookies for the `fanbox.cc`
domain is your best bet.

### Headers
This downloader sets an `Origin` header override for you. This is necessary to
access the Fanbox API.

You must also manually add a `User-Agent` header for the `fanbox.cc` domain,
or else you will be blocked by Cloudflare. Make sure it *exactly matches* the
value that the browser you get your cookies from uses. This downloader can't
set this for you.

## Tips for dealing with Cloudflare 

Since Cloudflare is so opaque about whether they think your web activity is
botted, all of these are just things that are known to make it less likely
for you to encounter 403 errors or unparseable pages:

* Log into Fanbox and browse/click around a bit before sending your cookies
  to Hydrus. The mouse activity makes you seem more human to Cloudflare's
  heuristics.
* Keep your Fanbox subscriptions paused most of the time; when you are ready
  to catch up on your Fanbox subs, send new cookies per the previous bullet
  point first, then unpause your fanbox subs, and then pause them again once
  they are complete. If you forget to pause, your subscriptions will probably
  wake up and run at some point when your Cloudflare cookies are invalid. In
  this case, you can _try_ retrying failed/ignored URLs in the subscriptions
  UI, or you can use a gallery downloader to catch up.
* Keep your IP address consistent between connections made by your browser and
  by Hydrus.
* If you use a VPN, you may need to disable it before logging into Fanbox to
  get your cookies, and you may need to make keep it disabled while your subs
  are running. If you are a power user, you may have some luck with split
  tunnels or a dedicated outbound proxy with a stable IP address, but the
  average Joe should just disable their VPN when it's "Fanbox time," then
  re-enable it afterward. 
* If you still run into issues:
  * Add stricter request/bandwidth limits for these domains, as necessary
    (note: only really applies if you override Hydrus' defaults or set custom
    values for these domains before):
    * `fanbox.cc`
    * `downloads.fanbox.cc`
    * `api.fanbox.cc`
  * Double-check that your cookies are fresh and that you're not getting
    the captcha page when loading Fanbox in your browser. If Cloudflare is
    testing that you're a human frequently enough, give up on subscriptions
    and just use a gallery downloader page.
  * Triple-check that your `User-Agent` header matches your browser's. If your
    browser auto-updates, you'll need to stay on top of when that happens.
  * If it's still not working, try seeking community help in Discord.

If you learn of any cool tricks to deal with the Cloudflare protection,
_please, do not hesitate to share them!_
