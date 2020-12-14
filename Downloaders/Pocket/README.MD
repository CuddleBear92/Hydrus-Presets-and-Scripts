This downloader will download any unread link saved to your Pocket account, assuming Hydrus can parse it. Now you can send links to your client from any device, anywhere! Well, more or less.

Of course, it's not as easy as import-and-go, it does require a bit of setup.

1. Go to the [Pocket developer page](https://getpocket.com/developer/) and click "Create New App".
	+ Select the "Retrieve" permission and "Web" platform.
2. Generate an access token for your account using your app's consumer key.
	+ There are tools on the internet to do this for you. I use [fxneumann's OneClickPocket](http://reader.fxneumann.de/plugins/oneclickpocket/auth.php).
3. In Hydrus, create a new "pocket saved articles" subscription, entering your consumer key followed by your access token as search terms.
	+ Search terms should be similar to: consumer-key access-token