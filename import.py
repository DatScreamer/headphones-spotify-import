######################################################
#
# Script created by DatScreamer.
#
#
# Prerequisites:
#   Exportify CSV file named all.csv (https://rawgit.com/watsonbox/exportify/master/exportify.html)
#   Headphones with enabled API (Settings>Web Interface>API>Enable API) (https://github.com/rembo10/headphones)
#   Python (Hasn't been tested on any version lower than 3.62) (https://www.python.org/)
#   Python Requests (May require pip to install on windows, setup is easiest on linux in my opinion.) (http://docs.python-requests.org/en/master/user/install/))
#
# Instructions:
#   1. Open Spotify (I used the desktop client) and create a new playlist with all the music you want to download. I went into "Songs" (Spotify>Songs) and selected everything with Ctrl+A then dragged the selection to the playlist in the sidebar.
#   2. Open your web browser and go to https://rawgit.com/watsonbox/exportify/master/exportify.html. Log in with your Spotify account and click export on your desired playlist.
#   3. Move the .csv file that you just downloaded to the same folder as importer.py and make sure it's named "all.csv"
#   4. Download and install Python, and Python Requests from the links in Prerequisites.
#   5. Install Headphones on whatever device you like, as long as it's on the same network as you are running the script on. If Headphones seemingly hasnt installed correctly and the webpage won't load you may need to edit the "config.ini" and change the host gateway (or whatever it's called.) from "localhost" to "0.0.0.0". This allows for headphones to run and be accessable on the network rather than just the local machine.
#   6. Setup Headphones. Go into the settings and configure your download settings, search provider settings, quality settings, etc...
#   7. Enable the API on Headphones. Go to Settings>Web Interface and enable the API.
#   8. Generate an API key from above webpage. And set your host and api key below.
#   9. You may need to use a Mirror domain for Musicbrainz if the musicbrainz searching is taking extended periods of time. If this is the case you can change it via Settings>Advanced Settings. I use the folling settings: Musicbrainz Mirror: Custom | Host: musicbrainz-mirror.eu | Port: 5000 | Required Authentication: No (unchecked) | Sleep Interval: 1
#   10. Am I missing anything? Lol. Don't think so. Let me know if you need help though.
#   11. Open terminal/command-line and navigate to the folder where all.csv and inporter.py are located.
#   12. Run this file. (importer.py)
#   13. Wait. It may take a really long time to complete the script, depending on your music library size.
######################################################'

host = "" # eg. myserver.com:8181, localhost:8181
apikey = "" # your api key from headphones


import csv
import json
import requests
import time
import pip

def install(colorama):
    pip.main(['install', package])

import colorama
colorama.init()
start = "\033[0;0m"
error = "\033[1;31m"
success = "\033[1;32m"
warning = "\033[1;33m"

if host == "" or apikey == "":
    # print (error + "Error. Enter Host and API key in this file (import.py).")
    input()

else:

    print (start + "Caution: This may take a very long time to complete, Depending on your music library size.")
    print (start + "Warning: This script does not support individual songs. It downloads the entire album that each of your songs are a part of.")
    print (start + "Waiting...")
    time.sleep(5)
    print (start + "Starting in...")
    time.sleep(1)
    print(start + "5..")
    time.sleep(1)
    print(start + "4..")
    time.sleep(1)
    print(start + "3..")
    time.sleep(1)
    print(start + "2..")
    time.sleep(1)
    print(start + "1..")
    time.sleep(1)
    print (start + "Starting!")

    f = open('all.csv')

    csv_f = csv.reader(f)
    if 'f' in locals():
        print (start + "Starting Up!")
    else:
        print (error + "Error. Failed to start up.")

    for row in csv_f:
        print (start + "#####################################")
        print (start + "Getting info from file.")
        artist = row[2]
        albumname = row[3]
        if 'artist' in locals():
            print (start + "Successfully retreived artist from file.")
        else:
            print (error + "Failed to read file.")

        if 'albumname' in locals():
            print (start + "Successfully retreived album from file.")
        else:
            print (error + "Failed to read file.")
        print (start + "Return:", artist, "-", albumname)
        payload = {'cmd': 'findAlbum', 'name': '%s - %s' % (albumname, artist)}

        r = requests.get('http://' + host + '/api?apikey=' + apikey, params=payload)
        status = r.status_code
        if status == 200:
            print (start + "Successfully got JSON!")
        else:
            print (warning + r.status_code)
        print (start + "Commencing Musicbrainz search!")
        json_obj = r.text
        readable_json = json.loads(json_obj)
        for i in readable_json:
            if i['title'].startswith(albumname) and i['uniquename'].startswith(artist):
                matchFoundTitle = i['title']
                matchFoundAlbumID = i['albumid']
                searchStatus = "resultFound"

                print (success + "Found matching album:", matchFoundTitle)
                print (start + "Got relating Album ID for",matchFoundTitle,":",matchFoundAlbumID)
                print (start + "Adding album to Headphones...")
                payload2 = {'cmd': 'addAlbum', 'id': '%s' % (matchFoundAlbumID)}

                r = requests.get('http://' + host + '/api?apikey=' + apikey, params=payload2)
                status = r.status_code
                if status == 200:
                    print (success + 'Successfully added album to "Wanted"!')
                else:
                    print (warning + r.status_code)

                break

            else:
                searchStatus = "resultNotFound"

        if searchStatus == "resultNotFound":
            print (error + 'Failed to match result with Musicbrainz.')

    print (success + "Finished!! We are done sending things to download!")
    exit()
    f.close()
