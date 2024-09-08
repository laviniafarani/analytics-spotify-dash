from utils import spotify_connection as sp

def get_user_name():
    name = str(sp().current_user()['display_name'])
    return name
