from utils import spotify_connection as sp
import pandas as pd

def get_user_top_tracks(limit=25, time_range='short_term'):
    '''
    long_term: (calculated from ~1 year of data and including all new data as it becomes available),
    medium_term: (approximately last 6 months)
    short_term: (approximately last 4 weeks)
    '''
    if not (3 <= limit <= 25):
        raise ValueError("The 'limit' parameter must be between 3 and 25. Default is 25.")

    user_top_tracks = sp().current_user_top_tracks(
        limit=limit,
        time_range=time_range
    )['items']

    user_top_track_data = [
        [
            track['id'],
            track['name'],
            track['artists'][0]['id'],
            track['artists'][0]['name'],
            track['album']['id'],
            track['album']['name'],
            track['album']['release_date'],
            track['album']['images'][0]['url'],
            track['external_urls']['spotify']
        ]
        for track in user_top_tracks
    ]
    user_top_tracks_columns = [
        'track_id', 'track_name', 'artist_id', 'artist_name',
        'album_id', 'album_name', 'release_year', 'song_image_url','song_url'
    ]
    df_user_top_tracks = pd.DataFrame(user_top_track_data, columns=user_top_tracks_columns)
    df_user_top_tracks['release_year'] = df_user_top_tracks['release_year'].str[:4]

    return df_user_top_tracks


def get_tracks_audio_features(tracks_id):
    audio_features = sp().audio_features(tracks_id)
    df_audio_features = pd.DataFrame(audio_features)

    return df_audio_features
