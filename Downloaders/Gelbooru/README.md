[See the help files for how to add downloaders to Hydrus](https://hydrusnetwork.github.io/hydrus/help/adding_new_downloaders.html)

This header sets the required `fringeBenefits=yup` cookie that lets you access blacklisted tags and other saucy content.

The _fringe benefits_ setting is not stored with your account (even when logged in), only as a cookie, which is why you either have to set it in your browser and then import the cookie into Hydrus or use this header.

# Api Basics

See [Api Basics Documentation] (https://gelbooru.com/index.php?page=wiki&s=view&id=18780) for an overview of the gelbooru api.

1. Import the api downloader to your client.
2. Obtain your api_key and user_id from [Gelbooru options] (https://gelbooru.com/index.php?page=account&s=options)
3. Open Hydrus and navigate to 'network'->'downloader components'->'manage url classes'->gelbooru gallery page api'.
4. Under parameters change the placeholder defaults of 'api_key' and 'user_id' to your specific values. Double click these entries and leave the first two windows unchanged.
5. Apply the changes.
6. Select 'gelbooru tag search api' in a gallery downloader.
