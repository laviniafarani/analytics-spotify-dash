from dash import Dash, html
import dash_bootstrap_components as dbc
from template import *

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container(
    [
        dbc.Row(
            put_title()
        ),

        dbc.Row([
            ##### TOP SONGS #####
            dbc.Col(
                dbc.Container(
                    [
                        html.H2("Top Songs", className="sub-title-text"),
                        template_top_songs(0),
                        template_top_songs(1),
                        template_top_songs(2),
                        template_top_songs(3),
                        template_top_songs(4)
                    ], className="box"
                ),
                width=4,
            ),

            #### TOP ARTISTS ####
            dbc.Col(
                dbc.Container(
                    [
                        html.H2("Top Artists", className="sub-title-text"),
                        template_top_artists(0),
                        template_top_artists(1),
                        template_top_artists(2),
                        template_top_artists(3),
                        template_top_artists(4),
                        html.H3("Popularity", className="sub-title-text"),
                        template_pop_titles(),
                        template_popularity()
                    ], className="box"
                ),
                width=4,
            ),

        ])

    ],
    className="main-background",
    fluid=True
)


if __name__ == "__main__":
    app.run(debug=True)
