#You may use my client id and client secret its dump account but i suggest you to get your own and you may see the result  
#in your spotify.You may get ur client id and client secret in spotipy usingg same account as of the spotify 
import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "4a52d5f2a6d4439eb4d4e6c3923219d7"
CLIENT_SECRET = "1e60abfb5838499699e314985f8d2250"
song_url = []
song_list = []

date = input("Enter the date (YYYY-MM-DD): ")
year = date[:4]
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
billboard_header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
billboard_data = requests.get(url=URL, headers=billboard_header)
soup = BeautifulSoup(billboard_data.text, "html.parser")
songs = soup.select("li ul li h3")
for song in songs:
    song = song.get_text().strip()
    song_list.append(song)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="playlist-modify-private"
    )
)

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        url = result["tracks"]["items"][0]["uri"]
        song_url.append(url)
    except IndexError:
        pass

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"Billboard Hot 100 - {date}",
    public=False,
    description=f"Top 100 songs from Billboard on {date}"
)
playlist_id = playlist["id"]

for i in range(0, len(song_url), 100):
    sp.playlist_add_items(playlist_id, song_url[i:i+100])

print(f"✅ Playlist created: {playlist['external_urls']['spotify']}")
