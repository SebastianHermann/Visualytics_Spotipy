import os, sys, json, spotipy, webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

#>>>Note: When executing this file, the spotify user id has to be given in the terminal<<<

#Get the username from terminal
username = sys.argv[1]

#Spotify client developer id
SPOTIPY_CLIENT_ID='XXXXXXXXXXX'
#Spotify client secret
SPOTIPY_CLIENT_SECRET='XXXXXXXXXXX'
#Redirection path for authentication
SPOTIPY_REDIRECT_URI='XXXXXXXXXXX'

#creating an access token
try:
    token = util.prompt_for_user_token(username,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)

#Create our SpotifyObject
spotify_Object = spotipy.Spotify(auth=token)

user = spotify_Object.current_user()

#print(json.dumps(user,sort_keys=True,indent=4))

displayName = user['display_name']
follower = user['followers']['total']

while True:
    print()
    print(">>>Welcome to Spotipy "+ displayName+"!")
    print(">>>You have "+ str(follower)+" followers.")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    # Search for the artist
    if choice == "0":
        print("0")
        searchQuery = input("Ok, what's their name?:")
        print()

        searchResults = spotify_Object.search(searchQuery,1,0,"artist")
        print(json.dumps(searchResults, sort_keys=True,indent=4))
    # End the program
    if choice == "1":
        break
