from dash import html
import dash_bootstrap_components as dbc
from analytics import Artists, Tracks
from api import get_user_top_artists, get_user_top_tracks

tracks = Tracks(get_user_top_tracks())
artists = Artists(get_user_top_artists())


def put_title():
    return dbc.Col(
                html.H1("Your Spotify"),
                className="title-text"
            )



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


def template_top_artists(index):
    top_artists = artists.top_artist()
    return  dbc.Row([
                dbc.Col(
                    html.A(
                        html.Img(
                            src=top_artists.iloc[index]['artist_image_url'],
                            alt='Description of my image',
                            style={'width': '50%'},
                            className="image-artist-style"
                        ),
                        href=top_artists.iloc[index]['artist_url'],
                        target='_blank',
                        className= 'image-position',
                    ),
                    width=3
                ),
                dbc.Col(
                    [
                        html.Div(
                            top_artists.iloc[index]['artist_name'],
                            className="text-white"
                        )
                    ],
                    className="info-tops-position",
                    width=9
                )
            ],
            className='row-bottom-margin'
        )
