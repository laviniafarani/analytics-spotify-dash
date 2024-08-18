from spotipy.oauth2 import SpotifyOAuth
import spotipy
import os
from dotenv import load_dotenv


def spotify_connection():
    load_dotenv()

    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
    scope = [
        'user-top-read',
        'user-library-read',
        'user-read-recently-played',
        'user-read-currently-playing'
    ]

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret = client_secret,
            redirect_uri=redirect_uri,
            scope=scope
        )
    )

    return sp

