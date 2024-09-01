import pandas as pd

class Tracks:
    def __init__(self, df_top_tracks):
        self.df_top_tracks = df_top_tracks

    def top_tracks(self, track_limit=5):

        df_top_tracks = self.df_top_tracks[[
            'track_name',
            'artist_name',
            'tempo',
            'song_image_url',
            'song_url'
        ]].copy()
        return df_top_tracks.head(track_limit)


    def min_bpm(self):
        min_bpm = self.df_top_tracks[[
            'track_name',
            'artist_name',
            'tempo',
            'song_image_url',
            'song_url'
        ]].loc[self.df_top_tracks['tempo'].idxmin()]
        return min_bpm

    def max_bpm(self):
        max_bpm = self.df_top_tracks[[
            'track_name',
            'artist_name',
            'tempo',
            'song_image_url',
            'song_url'
        ]].loc[self.df_top_tracks['tempo'].idxmax()]
        return max_bpm
