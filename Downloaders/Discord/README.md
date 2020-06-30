You need an authorisation token to access what your Discord account can access.

1. Login to to Discord in either a browser of the Discord client.
2. Press `Ctrl+Shift+I`
3. Navigate to the **Network** tab and then click on the **XHR** button.
4. In the table click the line named library. Refresh if you don't see anything.
5. In the right section, under headers, look for the authorisation line.
6. Copy the text next to authorisation.
7. In Hydrus, navigate to the `network -> data -> manage http headers` through the toolbar.
8. Replace the "PUT TOKEN HERE" with the token you copied in step 6.