from analytics import Artists, Tracks
from api import get_user_top_artists, get_user_top_tracks


artists = Artists(get_user_top_artists())
tracks = Tracks(get_user_top_tracks())

print(artists.top_artist())
print(artists.max_pop())
print(artists.min_pop())
print(tracks.top_tracks())
print(tracks.top_tracks_features())
