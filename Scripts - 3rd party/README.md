Cover Extract script for archives (.zip .cbz .cbr .rar .7z) with ComicRack xml metadata embedded `comicinfo.xml`
It will extract files/pages in certain set PageTypes in ComicRack. 
By default it will pull `"FrontCover","InnerCover","BackCover"` but more can be supported by editing.
It also has a blacklist to not process the same file again, can also set a flag in the form of a ScannerInfo Metadata entry with the keyword of your choice.
Full filename and folder name support on writeout.
More archives can be supported if 7z supports the format.