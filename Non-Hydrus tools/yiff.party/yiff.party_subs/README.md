# yiff.party subscription convert
This script will convert an standard yiff.party export (from the extract UI on the website) and turn them into a Subscription for Hydrus all bundled into one.

## How to use and install
Grab your yiff.party follow list and export them, there will be a floppy-disk icon to export and import favorites on the site.
Select everything in the input export field and copy. 
Make a new text file in the same folder as the script called `yiff.party_favourites.txt` and paste the copied export text and save the text file.
After that just run the script either with CMD with `python generate_yiff.party_subs_0.01.py` or double clicking it. Python needs to be installed.
This will make a new text file called `yiff.party subscriptions.txt`
Copy the whole contents of this text file and import from clipboard under `Network>Downloaders>Manage Subscriptions`
This will add a new `0 yiff.party` subscription containing all your exported favorites.

This requires URL Classes for yiff.party creators to be set to GALLERY, a GUG to actually input the ID of the creator and a Parser like he API parser which grabs the files.

**NOTE** the API parser does no yet support inline files but we are working on this one.

# **IMPORTANT** **DOUBLE CHECK YOUR SUBSCRIPTION SETTINGS AFTER IMPORT THAT THEY ARE TO YOUR LIKING AND NEEDS!**

v0.02: Blacklists, rename old favorites export to the blacklist name listed in the script. By Default: `yiff_blacklist.txt`
This will make it so it will not make subs of already exported favorites, only making new ones you might have added since the last export.