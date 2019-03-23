# Spotify API using Python.
This short Python script retrieves data from Spotify using API, manipulate the data, then output the data into MS excel files  

## Getting Started with Spotify.
Go to https://developer.spotify.com/ , create an account. Simply log in, go to your “dashboard” and select “create client id” and follow the instructions. Spotify are not too strict on providing permissions compare to Facebook.
While You're in the homepage, go to https://open.spotify.com/collection/playlists to create a playlist in any name, then add in some random songs to that list.
![alt text](http://i63.tinypic.com/2qlfn8m.jpg)

## Installation.
Please install the follwoing dependencies:
```
pip install spotify
pip install pandas
```
## Run the Python script.
This script will scrawl three type of data, manipulate the data and write three separate csv spreadsheets.
```
    # song list for this year
    getYearSongList("2019")

    # chosen artist
    getArtistSongList("lady gaga")
    
    # get user playlist
    getUserSinglePlaylistInfo(user_name, 'Enter A PlayList ID Here') 
 ```
 Logs output to termial while running the script.
 ```
  Retrieving a song list for 2019......
  Please check 2019_song_list.csv file for the data.

  Retrieving a song list by lady gaga......
  Please check lady_gaga_song_list.csv file for the data.

  Retrieving information from Dao's Playlist......
  Please check Dao's Playlist.csv file for the data.
 ```
 
