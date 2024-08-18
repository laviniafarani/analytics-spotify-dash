from utils import spotify_connection as sp
import pandas as pd


def get_user_top_artists(limit=25, time_range='short_term'):
    '''
    long_term: (calculated from ~1 year of data and including all new data as it becomes available),
    medium_term: (approximately last 6 months)
    short_term: (approximately last 4 weeks)
    '''
    if not (3 <= limit <= 25):
        raise ValueError("The 'limit' parameter must be between 3 and 25. Default is 25.")

    user_top_artists = sp().current_user_top_artists(
        limit=limit,
        time_range=time_range
    )['items']

    user_top_artists_data = [
        [
            artist['id'],
            artist['name'],
            artist['popularity'],
            artist['images'][0]['url'],
            artist['external_urls']['spotify']
        ]
        for artist in user_top_artists
    ]
    user_top_artists_columns = [
        'artist_id', 'artist_name', 'popularity', 'artist_image_url', 'artist_url'
    ]
    df_user_top_artists = pd.DataFrame(user_top_artists_data, columns=user_top_artists_columns)

    return df_user_top_artists

