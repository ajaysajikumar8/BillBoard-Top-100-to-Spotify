import os
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="https://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    ))

result = spotify.search(q="track: Save your tears year: 2022",type="track")
pprint(result)
