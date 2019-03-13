# 3rd party scripts run outside of the [Hydrus](https://github.com/hydrusnetwork/hydrus/) Client.

## [Booru.org](https://booru.org/top) GUG Generator
This Generates GUG files from a list of [Booru.org](https://booru.org/top) subdomains for easy bulk import.

## Cover Extract
Cover Extract script for archives (.zip .cbz .cbr .rar .7z) with [ComicRack](http://comicrack.cyolito.com/) xml Metadata embedded `comicinfo.xml`
It will extract files/pages in certain set PageTypes in [ComicRack.](http://comicrack.cyolito.com/) 
By default it will pull `"FrontCover","InnerCover","BackCover"` but more can be supported by editing.
It also has a blacklist to not process the same file again, can also set a flag in the form of a ScannerInfo Metadata entry with the keyword of your choice.
Full filename and folder name support on write-out.
More archives can be supported if 7z supports the format.

## Find non-Webp
Will check all archives for images and writeout an .xml or .cbl file listing all archive names.
This is meant to be used with ComicRack to make ComicBookLists so it will easily give you the files in the client that messed up exporting.
This was made cause ComicRack dont have an option to search for page format types like webp images.
If CR crashes or stops its export, you will loose your export lists.
Only way to really manage what is converted or not inside CR would be with some sort of metadata like: genre:webp... which works but isnt amazing.
Issue with this is that there is no way to tell if its actually converted or not if the export is stopped for whatever reason after you tagged it.
This script will give you an alternative to that by making a list for you.

## [yiff.party](https://yiff.party/) subs
Extracts [yiff.party](https://yiff.party/) favorite exports (as exported from the site) and turns them into subscriptions for easy imports in [Hydrus](https://github.com/hydrusnetwork/hydrus/).

## Booru Mass Uploader
A Browser Script for [TamperMonkey](https://tampermonkey.net/) [GreaseMonkey](https://www.greasespot.net/) you can find the original [HERE](https://github.com/Seedmanc/Booru-mass-uploader)
This should be updated over time or can be by any user if they want to add support for more.
Doing a [pull-request](https://github.com/Seedmanc/Booru-mass-uploader/pulls) on the original git can also be helpful for everyone so it updates semi-automatically for everyone.

## IQDB_tagger
A Python script that allows for bulk upload of images on iqdb though image recognition.
This can output sidecar files next to the file for easy import or an url list for easy downloading of all data in Hydrus.