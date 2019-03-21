# -*- coding: utf-8 -*-
"""
Created on 03/21/2019
@author: DAO NGUYEN

"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import json

client_id = "721bda361edd4dc49585c5ce19d71083"
client_secret = "954261c8f8724355915be6401f564b2c"

def main():
    print("Retrieving by Artist Name")
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
    name = "{Artist Name}" #chosen artist
    result = sp.search(name) #search query
    result['tracks']['items'][0]['artists']

    print(result)
    with open('spotify_data.json', 'w') as outfile:
        json.dump(result, outfile)


if __name__ == '__main__':

    main()