# -*- coding: utf-8 -*-
"""
Created on 03/21/2019
@author: DAO NGUYEN

"""

import sys
import spotipy
import collections
from spotipy.oauth2 import SpotifyClientCredentials 
import spotipy.util as util
import pandas as pd 
import datetime
import csv


client_id = "721bda361edd4dc49585c5ce19d71083"
client_secret = "954261c8f8724355915be6401f564b2c"
user_name = "dao.nguyen425@yahoo.com"


'''
This function to retrieve a list of songs from my favarite artist, Lady Gaga, put all songs in a list
with key, value of name of song and album name, sort in alphabetical order by song. Finally write 
results to a CVS file.
'''
def getArtistSongList(artist_name):
    print("Retrieving a song list by {}......".format(artist_name))
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 

    results = sp.search(q = "artist:" + artist_name, type = "album")

    song_list =[]
    artist_list =[]

    # get all the albums' tracks
    for i in range(len(results['albums'])):
        album_id = results['albums']['items'][i]['id']

    # get album tracks
        tracks = sp.album_tracks(album_id)
        for track in tracks['items']:
            # check for duplicate song in the list
            if track['name'] not in song_list:
                # add song name from album name to list
                song_list.append(track['name'])
                artist_list.append(results['albums']['items'][i]['name'])

    data = {'Song Name':song_list, 'Album Name':artist_list}

    # sorted the song list in alphabetical order
    df = pd.DataFrame(data)
    df = df.sort_values(by='Song Name')

    # Write data to file (song name from album name)
    df.to_csv("{}_song_list.csv".format(artist_name.replace(' ', '_')), index=False)
    print("Please check {}_song_list.csv file for the data.\n".format(artist_name.replace(' ', '_')))

'''
This function retrive the first 100 songs of 2019 from Spotify including the song name, artist, the song id, popularity
and out put the csv file by the most pupularity first.

'''
def getYearSongList(year):
    artist_name = []
    track_name = []
    track_id = []
    popularity = []

    print("Retrieving a song list for {}......".format(year))
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 

    # getting songs of 2019
    for i in range(0,100,50):
        track_results = sp.search(q='year:' + year, type='track', limit=50,offset=i)
        for i, t in enumerate(track_results['tracks']['items']):
            artist_name.append(t['artists'][0]['name'])
            track_name.append(t['name'])
            track_id.append(t['id'])
            popularity.append(t['popularity'])
        
    data = {'Song Name':track_name, 'Artist':artist_name, 'Popularity':popularity, 'Track ID':track_id} 

    df = pd.DataFrame(data)
    df = df.sort_values(by='Popularity', ascending=False)

    # # Write data to file sorted by popularity
    df.to_csv("{}_song_list.csv".format(year), index=False)
    print("Please check {}_song_list.csv file for the data.\n".format(year))


'''
This function get the information from a user single album base on the album id
'''
def getUserSinglePlaylistInfo(user, playlist_id):
    play_list_name = []
    song_list = []
    time_added_list = []
    song_length = []

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlist = sp.user_playlist(user, playlist_id)

    # get the playlist name
    play_list_name.append(playlist['name'])
    print("Retrieving information from {}......".format(play_list_name[0]))
    # adding the playlist info
    for item in playlist['tracks']['items']:
        time_added_list.append(item['added_at'])
        track = item['track']
        song_list.append(track['name']) 
        song_length.append(trackDurationConverter(track['duration_ms']))
      
    data = {'Song Name':song_list, 'Time Added':time_added_list, 'Song Length':song_length} 
    df = pd.DataFrame(data)

    # # Write a single user playlist info to file
    df.to_csv("{}.csv".format(play_list_name[0]), index=False)
    print("Please check {}.csv file for the data.\n".format(play_list_name[0]))

'''
This function convert time from milliseconds to time format
'''
def trackDurationConverter(millis):
    millis = int(millis)
    seconds = (millis/1000)%60
    seconds = int(seconds)
    minutes = (millis/(1000*60))%60
    minutes = int(minutes)
    hours = (millis/(1000*60*60))%24
    hours = int(hours)

    if(hours > 0):
        time_format = '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
    else:
        time_format = '{}:{:02}'.format(minutes, seconds)
    return time_format

'''
Main function
'''
def main():

    # song list for this year
    getYearSongList("2019")

    # chosen artist
    getArtistSongList("lady gaga")
    
    # get user playlist
    getUserSinglePlaylistInfo(user_name, '5V1hnvX0xH8Rk16U8hordK') 

if __name__ == '__main__':

    main()