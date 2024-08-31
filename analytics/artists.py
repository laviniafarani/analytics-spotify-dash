import plotly.graph_objs as go


class Artists():
    def __init__(self, df_top_artists):
        self.df_top_artists = df_top_artists


    def top_artist(self, limit=5):
        df_top_artists = self.df_top_artists[[
            'artist_name',
            'artist_image_url',
            'artist_url',
            'popularity'
        ]].copy()
        return df_top_artists.head(limit)

    def min_pop(self):
        min_pop = self.df_top_artists[[
            'artist_name',
            'popularity',
            'artist_image_url',
            'artist_url'
        ]].loc[self.df_top_artists['popularity'].idxmin()]
        return min_pop

    def max_pop(self):
        max_pop = self.df_top_artists[[
            'artist_name',
            'popularity',
            'artist_image_url',
            'artist_url'
        ]].loc[self.df_top_artists['popularity'].idxmax()]
        return max_pop

