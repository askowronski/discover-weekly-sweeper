First, make sure you have python3 installed on your computer.

Next, use pip3 to install spotipy: pip3 install spotipy

Next, insert your specific spotify client id, client secret, disocover weekly playlist id, and the playlist we are adding to's id. 

Next, navigate to the spotify web developer website and edit the settings of your app. Add the following as the callback URL: http://localhost:8080

Next, in a terminal, navigate to the src directory. Run the following command: python3 sweep.py

You should be prompted for permission from sptofiy -- click yes/accept and boom your bot has run.