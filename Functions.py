# Here is where all of our sorting functions are
from Classes import Song
from Classes import Duration
import random

# Function 1: Old vs New
# This function must take one parameter of type list[Song] and return two dictionaries of songs, or "Playlists",
# one for old Songs (released 2000 or earlier) and one for new songs (2001 or later)
# Input: one parameter of type list[Song]
# Output: two playlists (dictionaries) of Songs
def playlist_oldvnew(songs:list[Song])-> dict:
    old_songs={} # Creates empty dictionary for old songs
    new_songs={} # Creates empty dictionary for new songs
    old_track=1
    new_track=1
    for song in songs: # Loops through every song object in the list of songs
        if song.year_released<= 2000: # Checks if the current song was released before 2000 or not
            old_songs[old_track] = song # increases track number by 1
            old_track = old_track+ 1 # If the song was released before 2000, then it's added to the old songs playlist
        else: # If the song was released any time after...
            new_songs[new_track] = song # The song is added to the new songs playlist
            new_track = new_track + 1 # increases track number by 1

    print("Playlist of Old Songs")
    for song in old_songs: # This for loop fixes the display so there is one song on each line
        print(song,":",old_songs[song])
    print("Playlist of New Songs")
    for song in new_songs:  # This for loop fixes the display so there is one song on each line
        print(song, ":", new_songs[song])
    #return print("Old Songs:",old_songs,"New Songs:", new_songs) # returns both playlists

# Function 2: Duration
# Purpose: This function must take two parameters, one of type list[Song] and the other of type Duration.
# It must return a new list containing a "playlist" of sorts of the songs of which the input's duration is less than or equal to the second parameter type duration.
# Input: type list[Song} and type Duration
# Output: new list containing songs shorter than parameter Duration
def playlist_duration(songs: list[Song], total_time: Duration) -> list[Song]:
    playlist = [] # creates empty list for output
    for song in songs: # filtering through each iteration to check duration of each song
        if song.duration <= total_time: # if the song is less than the given time, then ---
            playlist.append(song) # append the song to new list if the song is less than the given duration
    return playlist # return the new playlist of songs


# Function 3: Shuffle Songs
# Purpose: This function must take one parameter, list[Song]and return a new list[Song] that has the Songs in a random order
# Input: list[Song]
# Output: new list[Song]
def playlist_shuffle_songs(songs:list[Song])-> dict:
    shuffled = songs[:]  # Make a copy of the list so we don't mess up the first one
    random.shuffle(shuffled)  # Shuffle it in-place, still with the same list
    shuffled_songs = {} # Make a dictionary of shuffled songs playlist
    track_number = 1 # Start the key at 1
    for song in shuffled:
        shuffled_songs[track_number] = song
        track_number = track_number + 1
    print("Shuffled Playlist:")
    for song in shuffled_songs:  # This for loop fixes the display so there is one song on each line
        print(song, ":", shuffled_songs[song])
    return shuffled_songs



