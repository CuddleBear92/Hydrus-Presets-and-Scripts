[See the help files for how to add downloaders to Hydrus](https://hydrusnetwork.github.io/hydrus/help/adding_new_downloaders.html)

# Patreon

This Patreon all-in-one handles Patreon creators and posts. It will get media and attachments from posts as well as some tags. It should also handle `patreon.com` creator and post links. It will only get posts your account has access to.

## Login Setup

The logins script will attempt to log you in through the API. Because of how it works you need to provide your login information in a specific format:

```json
{"type":"user","attributes":{"email":"user@example.com","password":"XXXXXXXXXXXXXXXX"}}
```

Replace `user@example.com` with your email and `XXXXXXXXXXXXXXXX` with your password. 

![image](https://user-images.githubusercontent.com/1300395/100398049-84c54f00-3012-11eb-961d-37f22aff48ec.png)

You may have trouble logging in if you haven't logged in from the same computer in a while. It may send a verification email, you will need to open the link there and retry the login in Hydrus. The login script won't work if you have two-factor authentication enabled. In that case, just use the `session_id` cookie from your browser. 

## Using the GUGs

### patreon creator search

This GUG attempts to use the third-party search service used by Patreon to find a creator's campaign. It searches for the creator (username or campaign name should work) and sends the first result on to the creator API parser. This should continue working but I'm not completely sure the API won't randomly change. So I suggest finding the campaign ID and using one of the other GUGs for long-term subscriptions.

### patreon api campaign

This is the most basic GUG and gets all posts from a given campaign ID. This campaign ID is different from the user ID used by some other sites that track Patreon content.

To find the campaign ID for a specific creator you can open their page (eg `patreon.com/creator`) and view source. There find the `<script>` tag which contains a bunch of JSON and look for the `"creator"` object. It will have an `id` attribute. You can test that you have the correct ID by appending it to `https://patreon.com/api/campaigns/` and looking at the JSON returned. 

### patreon api campaign (with tag)

This one gets posts by a given campaign ID filtered to a specific tag separated by a space.

### patreon api campaign (with tier filter)

This one gets posts by a given campaign ID filtered to a specific tier ID separated by a space.

You can find the tier ID by going to the creator's page on Patreon, filtering by the tier and looking at what follows `&filters[tier_id]=` in the URL.

### patreon api campaign (with tier filter and all patrons)

Same as above but including posts available explicitly to "all patrons"
