import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

date = input(
    "Which year do you want to travel to ? Type the date in this format YYYY-MM-DD: ")

year = date.split("-")[0]
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
songs = soup.find_all("h3", class_="a-no-trucate")
songs_name = [song.getText().strip() for song in songs]
# print(songs_name)


spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="https://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    ))

user_id = spotify.current_user()["id"]

uri = []
for song in songs_name:
    result = spotify.search(q=f"track: {song} year:{year}", type="track")
    try:
        song_uri = result["tracks"]["items"][0]["uri"]
        uri.append(song_uri)
    except IndexError:
        print(f"{song} doesnt exist in Spotify. Skipped.")
print(uri)