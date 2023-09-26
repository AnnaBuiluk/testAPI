import requests
from user_factory import user_data
import time

def receive_token(work=200):
    token_data = user_data.TokenData()
    response = requests.post(token_data.url_token, data=token_data.data)
    if response.status_code == 200:
        token_info = response.json()
        access_token = token_info.get('access_token')
        if work == 200:
            return access_token
    else:
        time.sleep(5)
        work = 0
        return receive_token(work)
