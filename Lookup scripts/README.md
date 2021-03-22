# File lookup scripts
## WARNING: SEMI-LEGACY FEATURE
File lookup scripts was part of the prototyping for the current downloader system but has been mostly left behind and unsupported since. It works even if it's a bit clunky and missing in features available in the actual downloader system these days. Don't expect much of it or support in regards to it.

To activate the feature you have to enable it somewhere in `file -> options`, it's named appropriately so just look through the options. Once it's enabled you'll find it in the `manage tags`-window for **single** files, it's literally one file at a time only. No bulk actions or automation whatsoever and it doesn't associate URLs either.

These days, thanks to the API, we mostly recommend people to use external programs to handle this. See [links here](https://github.com/Zweibach/text/blob/master/Hydrus/tagLessFiles.md#using-iqdb-and-saucenao) or the `!iqdb` command in the Discord. These programs can do bulk and since it then passes URLs back to Hydrus (if you configure them to do so) the normal downloader system with all its benefits will handle it.