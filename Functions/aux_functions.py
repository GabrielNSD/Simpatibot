from dotenv.main import load_dotenv
import os

import requests
from requests.structures import CaseInsensitiveDict

load_dotenv()

spotify_token = os.environ['SPOTIFY_API_KEY']

client_id = os.environ['SPOTIFY_CLIENT_ID']
redirect_uri = os.environ['SPOTIFY_REDIRECT_URL']

print(type(spotify_token))

#playlist_id no https => playlist/playlist_id? <=
playlist_Id = '2hzpv5XKZnQSyu5Nf9eMMa'  # a ideia é usar uma playlist fornecida pelo usuário

# 'https://api.spotify.com/v1/playlists/playlistId/tracks?uris='
url = 'https://api.spotify.com/v1/playlists/' + playlist_Id + '/tracks?uris='

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer " + spotify_token


def is_link(arg):
    arg_list = arg.split()
    for item in arg_list:
        if 'https://open.spotify' in item:
            type_of_link(item)
            print(transform_to_uri(item))
            return [True, item]

    return [False]


#
def type_of_link(arg):
    arg_list = arg.split('/')
    if arg_list[3] == 'track':
        return arg_list[3]
    print(arg_list)


def transform_to_uri(link):
    # spotify:track:code
    splitted_url = link.split('/')
    splitted_code = splitted_url[4].split('?')
    transformed_uri = 'spotify%3A' + \
        splitted_url[3] + '%3A' + \
        splitted_code[0]  # spotify%3Atrack%3AtrackCode

    endpoint = url+transformed_uri
    resp = requests.post(url=endpoint, headers=headers)
    print(resp.json())
    print("aqui", resp.status_code)
    return transformed_uri

def get_authorization_url(client_id, redirect_uri):
    return 'https://accounts.spotify.com/authorize?response_type=code' + client_id + '&scope=playlist-modify-public&redirect_uri=' + redirect_uri

def get_code_from__spotify_auth():
    return requests.get(url=get_authorization_url(client_id, redirect_uri))

