import requests
from ModelRequest import *
import os
def call_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return None
def reset_table(url):
    requests.get(url)
def post_data(url,data):
    while True:
        try:
            response = requests.post(url,json=data.dict())
            response.raise_for_status()
            break
            return data
        except requests.exceptions.RequestException as e:
            print("Bạn hãy đợi API")
            return None