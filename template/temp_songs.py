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
