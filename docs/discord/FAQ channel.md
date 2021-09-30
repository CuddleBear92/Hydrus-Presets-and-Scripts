__**GENERAL**__
> ***What is Hydrus?***
> It's a file manager and downloader based on hash values and tags.
> It allows for easy management of tags for almost any file, primarily images.
> But is made for file from the online web, like a booru or imageboard.

> ***My Antivirus says this is bad! Is it!?***
> No. It's a false positive caused by many viruses using the same common Python libraries Hydrus (and other software) uses for its network functionality.
> Check with <https://www.virustotal.com> for confirmation.

> ***My question isn't covered in this shitty FAQ.***
> Not a question. Use the Discord __*Search feature!*__
> Explorer the UI yourself and just TRY. Read the manual. It is extensive and offers answers and explanations to the majority of the features.

> **That didn't help.**
> Then ask in #support (and read the manual). Also, still not a question.


__**DOWNLOAD SYSTEM**__
> ***Why doesn't Pixiv work?***
> You may be required to be logged on to Pixiv. For Hydrus you need to both import the Pixiv cookies from your browser and copy the browsers exact user-agent.
> Read this guide: <https://github.com/Zweibach/text/blob/master/Hydrus/Sites/Pixiv.md>

> ***Why doesn't Tumblr work?***
> Try turning on the GDPR option under `network > logins > DEBUG: do tumblr GDPR click-through`.

> ***How do I download from SadPanda?***
> Import the preset and copy over your cookies from your browser.
> Or if you're an advanced user: <https://github.com/imtbl/hex>

> ***How do I import tags from a website?***
> Read the manual: <https://hydrusnetwork.github.io/hydrus/help/getting_started_downloading.html#parsing_tags>
 
> ***Where do I find new Download Presets?***
> At the presets GitHub page: <https://github.com/CuddleBear92/Hydrus-Presets-and-Scripts/tree/master/Downloaders>

> ***How do I import a Preset .png image file?***
> Read the manual: <https://hydrusnetwork.github.io/hydrus/help/adding_new_downloaders.html>

> ***How do I scrape/download a whole site?***
> Hydrus is not built with this sort of extensive scraping in mind but it may work for some sites, but requires a lot of work.
> **a)** Manually generate (copy) all the relevant URLs from the website and make a list in your text editor. Put only one URL per line. Once your list is complete copy the entire list and import them into a Hydrus *URL Import* page. Click the clipboard icon :hydrus_paste_clipboardicon: next to the input field to paste them in bulk for import.
> **b)** __Recommended__: Use a tool that is designed for this purpose. There are plenty of website scraping tools available if you search for it.

> ***How do I access restricted content?***
> Depending on the site you can just log on from within Hydrus. Some methods include:
> **a)** Login scripts: Navigate to `network > logins` and add your login details to he site in question if one exists. If a login script doesn't exist you may create one yourself (advanced).
> **b)** Import cookies: If your web browser is already logged on you can export its session cookies and import these into Hydrus. Hydrus directly supports the Netscape/Mozilla cookie file format.
> **c)** __Recommended__: Setup the Hydrus API, then download and install the Hydrus Companion browser extension and configure it with the API details. This allows you to easily transfer cookies directly into Hydrus with a click.
> *Hydrus API manual: <https://hydrusnetwork.github.io/hydrus/help/client_api.html>*
> *Hydrus Companion: <https://gitgud.io/prkc/hydrus-companion>*


__**TAGS**__
> ***Can I make siblings/parents for namespaces?***
> No. <https://github.com/hydrusnetwork/hydrus/issues/589>  

> ***How do I automatically get tags for files?***
> Read this guide: <https://github.com/Zweibach/text/blob/master/Hydrus/tagLessFiles.md>


__**DUPLICATE SYSTEM**__
> ***Can I dupe search videos/.gif?***
> No. <https://github.com/hydrusnetwork/hydrus/issues/160>


__**Links**__
> GitHub: <https://github.com/hydrusnetwork/hydrus>
> Presets & Scripts: <https://github.com/CuddleBear92/Hydrus-Presets-and-Scripts>
> PTR FAQ: <https://github.com/Zweibach/text/blob/master/Hydrus/PTR.md>
> PTR Quicksync: <https://koto.reisen/quicksync/>
> Tumblr: <http://hydrus.tumblr.com/>
> Twitter: <https://twitter.com/hydrusnetwork>
> Patreon: <https://www.patreon.com/hydrus_dev>
> E-mail: hydrus.admin@gmail.com or (`@hydrus_dev#5313`) for direct messaging on Discord.


__**Other useful Links:**__
> The fucking manual: <https://hydrusnetwork.github.io/hydrus/help/>
> The simple manual: <https://github.com/Zweibach/text/blob/master/Hydrus/Hydrus%20Help%20Docs/00_tableOfContents.md>
> The video manual: <https://github.com/CuddleBear92/Hydrus-guides>
