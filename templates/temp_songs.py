from dash import html, dcc
import dash_bootstrap_components as dbc
from analytics import Tracks
from api import get_user_top_tracks


tracks = Tracks(get_user_top_tracks())

def template_top_songs(index):
    top_songs = tracks.top_tracks()
    return  dbc.Row([
                dbc.Col(
                    html.A(
                        html.Img(
                            src=top_songs.iloc[index]['song_image_url'],
                            alt='Description of my image',
                            style={'width': '50%'},
                            className="image-song-style"
                        ),
                        href=top_songs.iloc[index]['song_url'],
                        target='_blank',  # Opens the link in a new tab
                        className= 'image-position',
                    ),
                    width=3
                ),
                dbc.Col(
                    [
                        html.Div(top_songs.iloc[index]['track_name'], className='text-white'),
                        html.Div(top_songs.iloc[index]['artist_name'], className='text-gray')
                    ],
                    className="info-tops-position",
                    width=9
                )
            ],
            className='row-bottom-margin'
        )


def template_bpm():
    min_track_bpm = tracks.min_bpm()
    max_track_bpm = tracks.max_bpm()
    return  dbc.Row([
                    ###  Min Pop
                    dbc.Col(
                        html.A(
                            html.Img(
                                src=min_track_bpm['song_image_url'],
                                alt='Description of my image',
                                style={'width': '50%'},
                                className="image-song-style"
                            ),
                            href=min_track_bpm['song_url'],
                            target='_blank',
                            className= 'image-position',
                        ),
                        width=3
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                min_track_bpm['track_name'], className="text-white"
                            ),
                            html.Div(
                                round(min_track_bpm['tempo'], 0), className="text-gray"
                            ),
                        ],
                        className="info-tops-position",
                        width=3
                    ),
                    ### Max Pop
                    dbc.Col(
                        html.A(
                            html.Img(
                                src=max_track_bpm['song_image_url'],
                                alt='Description of my image',
                                style={'width': '50%'},
                                className="image-song-style"
                            ),
                            href=max_track_bpm['song_url'],
                            target='_blank',
                            className= 'image-position',
                        ),
                        width=3
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                max_track_bpm['track_name'], className="text-white"
                            ),
                            html.Div(
                                round(max_track_bpm['tempo'],0), className="text-gray"
                            ),
                        ],
                        className="info-tops-position",
                        width=3
                    )
            ],
            className='row-bottom-margin'
        )
