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

## [yiff.party](https://yiff.party/) subs
Extracts [yiff.party](https://yiff.party/) favorite exports (as exported from the site) and turns them into subscriptions for easy imports in [Hydrus](https://github.com/hydrusnetwork/hydrus/).

## Booru Mass Uploader
A Browser Script for [TamperMonkey](https://tampermonkey.net/) [GreaseMonkey](https://www.greasespot.net/) you can find the original [HERE](https://github.com/Seedmanc/Booru-mass-uploader)
This should be updated over time or can be by any user if they want to add support for more.
Doing a [pull-request](https://github.com/Seedmanc/Booru-mass-uploader/pulls) on the original git can also be helpful for everyone so it updates semi-automatically for everyone.

## IQDB_tagger
A Python script that allows for bulk upload of images on iqdb though image recognition.
This can output sidecar files next to the file for easy import or an url list for easy downloading of all data in Hydrus.