import requests
from bs4 import BeautifulSoup

date = input(
    "Which year do you want to travel to ? Type the date in this format YYYY-MM-DD: ")

url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
songs = soup.find_all("h3", class_="a-no-trucate")
songs_name = [song.getText().strip() for song in songs]
print(songs_name)
