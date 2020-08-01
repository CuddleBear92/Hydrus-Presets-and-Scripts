This downloader uses Google's Google Drive API to parse and download files and folders on Google Drive. 

In order to use this downloader, a Google Drive API key is necessary. These instructions will teach you how to generate and add an API key to the parser.

1. Import this downloader to your client. This should be obvious, but I want to cover all bases.
2. Go to the [Google API Console](https://console.developers.google.com/) in your web browser.
3. Create a new project for your API use. You can name the project anything you want, but I recommend giving it a name you'll be able to recognize.
	+ If you have no other projects, there will be a blue button to the right of the page which says "Create Project"
	+ If you have created projects before, a new one be created by clicking "Select Project," and clicking the "New Project" button in the upper-right corner of the popup.
4. You will land on the "APIs & Services" page. Click "Enable APIs and Services" and scroll down until you see "Google Drive API" under the heading "G Suite." Click it and select "Enable" on the next page.
5. Now you will land on the API overview page. Click "Credentials" in the bar to the left of the page, and then "Create Credentials" at the top of the Credentials page. In the dropdown box that appears, select "API Key". Copy the key that appears in the popup.
	+ The popup will warn you to restrict your API key for security. If you don't plan to use this project for anything else, this is unnecessary.
6. In your Hydrus client, navigate to the "Manage URL Classes" dialoge and edit "google drive file download api".
7. Under "Parameters", you will see one named "key" with the default value of "YourKeyHere". Edit this key, clicking through until you reach the default value. Replace "YourKeyHere" with the key you copied in step 5.
8. Repeat step 7 for the following URL classes:
	+ google drive file download api (v2)
	+ google drive file get api
	+ google drive file list api
	+ google drive file list api (page 2+)
	+ (Optional) You can also add your keys to the example URLs in the parsers if you plan to test or edit them there.
	
After completing these steps, you should be ready to download files and folders from Google Drive.

This downloader does not include bandwidth rules, but if you need to download more per day, feel free to increase data limits for googleapis.com, as Google's services are very liberal in this regard.

Reach me on Hydrus Discord @Ganbat if I screwed something up.