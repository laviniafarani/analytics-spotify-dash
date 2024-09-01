from dash import html, dcc
import dash_bootstrap_components as dbc


def put_title():
    return dbc.Col(
                html.H1("Your Spotify"),
                className="title-text"
            )


def template_pop_titles():
    return dbc.Row([
        dbc.Col(html.Div('Least Popular', className="sub-sub-title-text")),
        dbc.Col(html.Div('Most Popular', className="sub-sub-title-text")),
    ])

def template_bpm_titles():
    return dbc.Row([
        dbc.Col(html.Div('Lowest BPM', className="sub-sub-title-text")),
        dbc.Col(html.Div('Highest BPM', className="sub-sub-title-text")),
    ])


