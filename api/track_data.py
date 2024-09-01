from utils import spotify_connection as sp
import pandas as pd

def get_user_top_tracks(limit=25, time_range='short_term'):
    '''
    long_term: (calculated from ~1 year of data and including all new data as it becomes available),
    medium_term: (approximately last 6 months)
    short_term: (approximately last 4 weeks)

    https://developer.spotify.com/documentation/web-api/reference/get-audio-features
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

    audio_features = sp().audio_features(df_user_top_tracks['track_id'])
    df_audio_features = pd.DataFrame(audio_features)

    tracks_info = pd.merge(
        df_user_top_tracks,
        df_audio_features,
        left_on='track_id',
        right_on='id'
    )
    columns=[
        'track_name', 'artist_name', 'album_name',
        'danceability', 'valence', 'energy', 'tempo',
        'key', 'mode', 'time_signature', 'loudness',
        'speechiness', 'instrumentalness','acousticness',
        'liveness', 'duration_ms', 'release_year',
        'track_id', 'artist_id', 'song_image_url','song_url'
    ]

    return tracks_info[columns]
