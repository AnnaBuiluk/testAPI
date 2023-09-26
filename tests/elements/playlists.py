import time
import datetime
import requests
from . import token_creation
from user_factory import user_data


def get_user_playlists(limit):
    url = user_data.url_base + "/me/playlists"
    # limit = 100
    token = token_creation.receive_token()
    headers = {'Authorization': f'Bearer {token}'}
    params = {"limit": limit}
    response = requests.get(url, headers=headers, params=params)
    response = response.json()
    return response


#     pprint.pprint(response)
#     print(len(response.get('items')))
#
#
# get_user_playlists()

def create_a_playlist(name=''):
    if not name:
        name = "My Playlist from test " + str(datetime.datetime.now())
    url = user_data.url_base + "/me/playlists"
    token = token_creation.receive_token()
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        "name": name,
        "trackIds": [
            "565880", "566595", "119962", "523487"
        ]
    }
    response = requests.post(url, json=data, headers=headers)
    response = response.json()
    return response


def get_playlist_by_id(id):
    url = user_data.url_base + "/me/playlists/" + str(id)
    token = token_creation.receive_token()
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    response = response.json()
    return response


def remove_playlists(id):
    url = user_data.url_base + "/me/playlists/" + str(id)
    token = token_creation.receive_token()
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(url, headers=headers)
    # response = response.json()
    # return response


def rename_playlists(id,name):
    url = user_data.url_base + "/me/playlists/" + str(id)
    token = token_creation.receive_token()
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        "name": name
    }
    response = requests.patch(url,json=data, headers=headers)
    # response = response.json()
    # return response
