import pandas as pd
from api import get_tracks_audio_features

class Tracks:
    def __init__(self, df_top_tracks):
        self.df_top_tracks = df_top_tracks  #get_user_top_tracks()

    def top_tracks(self, track_limit=5):

        df_top_tracks = self.df_top_tracks[[
            'track_name',
            'artist_name',
            'song_image_url',
            'song_url'
        ]].copy()
        return df_top_tracks.head(track_limit)


    def top_tracks_features(self):
        ''' https://developer.spotify.com/documentation/web-api/reference/get-audio-features'''

        df_track_features = get_tracks_audio_features(self.df_top_tracks['track_id'])

        tracks_info = pd.merge(
            self.df_top_tracks,
            df_track_features,
            left_on='track_id',
            right_on='id'
        )
        columns=[
            'track_name', 'artist_name', 'release_year',
            'danceability', 'valence', 'energy', 'tempo',
            'key', 'mode', 'time_signature', 'loudness',
            'speechiness', 'instrumentalness','acousticness',
            'liveness', 'duration_ms'
        ]
        return tracks_info[columns]




