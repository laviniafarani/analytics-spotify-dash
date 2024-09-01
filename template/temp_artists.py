from dash import html, dcc
import dash_bootstrap_components as dbc
from analytics import Artists
from api import get_user_top_artists

artists = Artists(get_user_top_artists())

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
                            top_artists.iloc[index]['artist_name'], className="text-white"
                        ),
                    ],
                    className="info-tops-position",
                    width=9
                )
            ],
            className='row-bottom-margin'
        )


def template_popularity():
    min_pop_artist = artists.min_pop()
    max_pop_artist = artists.max_pop()
    return  dbc.Row([
                    ###  Min Pop
                    dbc.Col(
                        html.A(
                            html.Img(
                                src=min_pop_artist['artist_image_url'],
                                alt='Description of my image',
                                style={'width': '50%'},
                                className="image-artist-style"
                            ),
                            href=min_pop_artist['artist_url'],
                            target='_blank',
                            className= 'image-position',
                        ),
                        width=3
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                min_pop_artist['artist_name'], className="text-white"
                            ),
                            html.Div(
                                min_pop_artist['popularity'], className="text-gray"
                            ),
                        ],
                        className="info-tops-position",
                        width=3
                    ),
                    ### Max Pop
                    dbc.Col(
                        html.A(
                            html.Img(
                                src=max_pop_artist['artist_image_url'],
                                alt='Description of my image',
                                style={'width': '50%'},
                                className="image-artist-style"
                            ),
                            href=max_pop_artist['artist_url'],
                            target='_blank',
                            className= 'image-position',
                        ),
                        width=3
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                max_pop_artist['artist_name'], className="text-white"
                            ),
                            html.Div(
                                max_pop_artist['popularity'], className="text-gray"
                            ),
                        ],
                        className="info-tops-position",
                        width=3
                    )
            ],
            className='row-bottom-margin'
        )
