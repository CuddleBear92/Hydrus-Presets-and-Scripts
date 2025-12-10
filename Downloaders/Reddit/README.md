Beware of the 100 Queries/10-Min API limit (only applies to .json queries, media eg. images and gifs are not counted)

To fetch private Cutom-Feeds you need to import your reddit cookies

Changelog 08.Nov.2025:
* Added support for posts with multiple files
* Added support for Custom-Feeds/MultiReddits through URL-Import
* Changed User & Subreddit search from 'hot' sorting to 'new'
* Changed User-Search to only fetch posts made BY the user, excluding posts where the user merely commented on
* Changed parsing to use the Feed-json primarily, removing the necessity for API-calls for each post
