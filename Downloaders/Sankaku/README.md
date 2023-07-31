[See the help files for how to add downloaders to Hydrus](https://hydrusnetwork.github.io/hydrus/help/adding_new_downloaders.html)

# API parser
Unlike the web frontend of Sankaku the API is not limited and can thus download a lot more in the same timeframe.

To ensure things work properly you will need to delete all bandwidth limits for Sankaku and the global limits. Depending on the size of your potential query you might need to either delete the limits for global too, or crank them up a fair deal. Bandwidth limits are found under `network -> data -> review bandwidth usage`.

The reason for this is that the URLs generated are only valid for a limited time (1h as of April 2021) so if you haven't downloaded them when they expire you'll only get trash.

## Search limitations
The Sankaku API is limited to 5000 items so any queries bigger than that will need to be done in batches by adding an offset.  
`1girl` for example will only get the first 5k item. Then, you have to look up the ID of the last post you downloaded. Adding `id_range:<=LAST_POST_ID` (E.g., `1girl id_range:<=42000`) will return the next 5k items.

## CAPI-V2 Auth
Since cookies do not work anymore, you have to manually add the auth bearer token to hydrus.
1. Open browser, loging into beta page
2. Open dev tools, go to network and reload the page
3. Search for the first `GET` request occurrence of keyset url in your network tab and open the headers tab of the details.
4. Create a new `authorization` HTTP HEADER in hydrus for the `capi-v2.sankakucomplex.com` domain. Copy the content of the `authorization` request header and paste it into the value field.
5. Update the header every 48 hours manually.
6. Do not forget to approve the HTTP header to be used.

For example:

![image](https://user-images.githubusercontent.com/1300395/160287848-9a5558e0-9a09-4289-891d-9088272b7ce8.png)

---

# Default parser
The default rules for the chan.sankaku default parser are a bit strict, if you find yourself running into issues with hitting the Hydrus limits too often you can relax them a bit. The table below shows a set of rules that are fairly relaxed and don't run into Sankaku's own bandwidth throttling. Going over those on the default parser will yield trash data rather than being outright rejected.

max allowed|every
-----|-----
1 requests|5.0 seconds
80 requests|7 minutes
