# -*- coding: utf-8 -*-
"""
Created on 03/21/2019
@author: DAO NGUYEN

"""

import sys
import spotipy
import collections
from spotipy.oauth2 import SpotifyClientCredentials 
import csv
import json

client_id = "721bda361edd4dc49585c5ce19d71083"
client_secret = "954261c8f8724355915be6401f564b2c"

def artist_song_list(artist_name):
    print("Retrieving song list by " + artist_name)
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 

    results = sp.search(q = "artist:" + artist_name, type = "album")

    song_list = {}
    check_list =[]

    # get all the albums' tracks
    for i in range(len(results['albums'])):
        album_id = results['albums']['items'][i]['id']
        # album_name = results['albums']['items'][i]['name']
        # print(album_name)
        

    # get album tracks
        tracks = sp.album_tracks(album_id)
        for track in tracks['items']:
            if track['name'] not in check_list:
                check_list.append(track['name'])
                song_list[track['name']] = results['albums']['items'][i]['name']


    song_list = dict(sorted(song_list.items()))

    print(song_list)
    # result = sp.search(name,) #search query
    # result['tracks']['items'][0]['artists']

    # #Extract Artist's uri
    # artist_uri = result['tracks']['items'][0]['artists'][0]['uri']
    # #Pull all of the artist's albums
    # sp_albums = sp.artist_albums(artist_uri, album_type='album')
    # #Store artist's albums' names' and uris in separate lists
    # album_names = []
    # album_uris = []
    # for i in range(len(sp_albums['items'])):
    #     if sp_albums['items'][i]['name'] not in album_names:
    #         album_names.append(sp_albums['items'][i]['name'])
    #         album_uris.append(sp_albums['items'][i]['uri'])

        
    # print(album_names)
    # print(album_uris)
    #Keep names and uris in same order to keep track of duplicate albums
    # Open File
    # resultFyle = open("{}_song_list.csv".format(name.replace(' ', '_')),'w')
    with open("{}_song_list.csv".format(artist_name.replace(' ', '_')), 'w') as f:

    # Write data to file
        for key in song_list.keys():
            f.write("%s,%s\n"%(key,song_list[key]))


def main():
    

    # chosen artist
    artist_song_list("lady gaga")
 

if __name__ == '__main__':

    main()