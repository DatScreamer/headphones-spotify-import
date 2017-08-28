Headphones Spotifty Import

---------------------------------------------------------

Notice: Due to the fact that Headphones relies on Musicbrainz to find information (artists, albums) we cannot garuntee that a song will be added to Headphones because of disparities between Spotify and Musicbrainz databases. Such as Spotify may have an album but Musibrainz may not but rather have only 2x songs from that album as singles.

---------------------------------------------------------

Prerequisites:
1. Exportify CSV file named all.csv (https://rawgit.com/watsonbox/exportify/master/exportify.html)
2. Headphones with enabled API (Settings>Web Interface>API>Enable API) (https://github.com/rembo10/headphones)
3. Python (Hasn't been tested on any version lower than 3.62) (https://www.python.org/)
4. Python Requests (May require pip to install on windows, setup is easiest on linux in my opinion.) (http://docs.python-requests.org/en/master/user/install/))

---------------------------------------------------------

Instructions:
1. Open Spotify (I used the desktop client) and create a new playlist with all the music you want to download. I went into "Songs" (Spotify>Songs) and selected everything with Ctrl+A then dragged the selection to the playlist in the sidebar.
2. Open your web browser and go to https://rawgit.com/watsonbox/exportify/master/exportify.html. Log in with your Spotify account and click export on your desired playlist.
3. Move the .csv file that you just downloaded to the same folder as importer.py and make sure it's named "all.csv"
4. Download and install Python, and Python Requests from the links in Prerequisites.
5. Install Headphones on whatever device you like, as long as it's on the same network as you are running the script on. If Headphones seemingly hasnt installed correctly and the webpage won't load you may need to edit the "config.ini" and change the host gateway (or whatever it's called.) from "localhost" to "0.0.0.0". This allows for headphones to run and be accessable on the network rather than just the local machine.
6. Setup Headphones. Go into the settings and configure your download settings, search provider settings, quality settings, etc...
7. Enable the API on Headphones. Go to Settings>Web Interface and enable the API.
8. Generate an API key from above webpage. Copy it and paste it into the two (YES. Two) lines titled "Change the below URL to the correct one. It may be something like "http://localhost:8181" or "https://192.168.0.17:8181". You Also need to change "apikey=yourapikey to the api key you generated via the instrustions"" below in this document.
9. You may need to use a Mirror domain for Musicbrainz if the musicbrainz searching is taking extended periods of time. If this is the case you can change it via Settings>Advanced Settings. I use the folling settings: Musicbrainz Mirror: Custom | Host: musicbrainz-mirror.eu | Port: 5000 | Required Authentication: No (unchecked) | Sleep Interval: 1
10. Am I missing anything? Lol. Don't think so. Let me know if you need help though.
11. Open terminal/command-line and navigate to the folder where all.csv and inporter.py are located.
12. Run this file. (importer.py)
13. Wait. It may take a really long time to complete the script, depending on your music library size.
