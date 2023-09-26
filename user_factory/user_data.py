url_base = "https://stash.nugsdev.net/api/v1"

class TokenData:
    url_token = "https://id.nugsdev.net/connect/token"
    client_id = "3TwoVlLAUFrJX33n3HSCSO"
    client_secret = "z5qkvc7ORNms7opUHRROPn"
    grant_type = "password"
    username = "annatest@gmail.com"
    password = "ANNAtest123"
    scope = "nugsnet:api nugsnet:legacyapi openid profile email"
    data = {
        'grant_type': grant_type,
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': password
    }
