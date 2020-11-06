# API parser
Unlike the web frontend of Sankaku the API is not limited and can thus download a lot more in the same timeframe.

To ensure things work properly you will need to delete all bandwidth limits for Sankaku. Depending on the size of your potential query you might need to either delete the limits for global too, or crank them up a fair deal.

The reason for this is that the URLs generated are only valid for a limited time (~24h) so if you haven't downloaded them when they expire you'll only get trash.

## Search limitations
The Sankaku API is limited to 5000 items so any queries bigger than that will need to be done in batches by adding an offset.  
`1girl` for example will only get the first 5k item. Then, you have to look up the ID of the last post you downloaded. Adding `id_range:<=LAST_POST_ID` (E.g., `1girl id_range:<=42000`) will return the next 5k items.

---

# Default parser
The default rules for the chan.sankaku default parser are a bit strict, if you find yourself running into issues with hitting the Hydrus limits too often you can relax them a bit. The table below shows a set of rules that are fairly relaxed and don't run into Sankaku's own bandwidth throttling. Going over those on the default parser will yield trash data rather than being outright rejected.

max allowed|every
-----|-----
1 requests|5.0 seconds
80 requests|7 minutes
