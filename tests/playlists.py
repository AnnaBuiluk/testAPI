import pytest
from elements import playlists
from elements import token_creation

def test_get_user_playlists_limit_100():
    element = playlists.get_user_playlists(100)
    assert element.get('limit') == 100

def test_get_user_playlists_limit_10():
    element = playlists.get_user_playlists(10)
    assert element.get('limit') == 10

def test_get_user_playlists_more_0():
    element = playlists.get_user_playlists(10)
    assert len(element.get('items')) >= 0
def test_create_a_playlist():
    element0 = playlists.get_user_playlists(100)
    el0 = element0.get('items')
    element = playlists.create_a_playlist()
    id = element.get("id")
    element1 = playlists.get_user_playlists(100)
    el1 = element1.get('items')
    result = list(filter(lambda item: item not in el0, el1))
    assert id in result[0]["id"]
 # and (element.get('total') == 10

def test_get_playlist_by_id_present():
    element = playlists.get_playlist_by_id("1275003")
    assert element.get('name') == "Test Remane Playlist and remove track"

def test_get_playlist_by_id_not_present():
    element = playlists.get_playlist_by_id("1")
    assert element.get('title') == "Not Found"


def test_remove_playlists_positive():
    #Check current playlists
    element0 = playlists.get_user_playlists(100)
    el0 = element0.get('items')
    #Create new playlist
    element = playlists.create_a_playlist()
    #Save id of this playlist
    id = element.get("id")

    # # Check playlists after add new playlist
    # element1 = playlists.get_user_playlists(100)
    # el1 = element1.get('items')
    # result = list(filter(lambda item: item not in el0, el1))
    # assert id in result[0]["id"]
    element = playlists.get_playlist_by_id(id)
    name = element.get("name")
    assert element.get('name') == name

    playlists.remove_playlists(id)

    element = playlists.get_playlist_by_id(id)
    assert element.get('title') == "Not Found"

def test_rename_playlists_positive():
    #Check current playlists
    element0 = playlists.get_user_playlists(100)
    el0 = element0.get('items')
    #Create new playlist
    element = playlists.create_a_playlist()
    #Save id of this playlist
    id = element.get("id")
    element = playlists.get_playlist_by_id(id)
    name = element.get("name")
    name = name + "abc"
    #Rename playlist
    playlists.rename_playlists(id, name)

    element1 = playlists.get_playlist_by_id(id)
    assert element1.get('name') == name





