# Here is where all of our sorting functions are
from Classes import Song
from Classes import Duration

# Function 1: Old vs New
# This function must take one parameter of type list[Song] and return two dictionaries of songs, or "Playlists",
# one for old Songs (released 2000 or earlier) and one for new songs (2001 or later)
# Input: one parameter of type list[Song]
# Output: two playlists (dictionaries) of Songs
def playlist_oldvnew(songs:list[Song])-> dict:
    old_songs={} # Creates empty dictionary for old songs
    new_songs={} # Creates empty dictionary for new songs
    for i in range(len(songs)-1): # Loops through every song object in the list of songs
        if songs[i].year_released<= 2000: # Checks if the current song was released before 2000 or not
            old_songs[i]=songs[i] # If the song was released before 2000, then it's added to the old songs playlist
        else: # If the song was released any time after...
            new_songs[i]=songs[i] # The song is added to the new songs playlist
    return print("old songs:",old_songs,"new songs:", new_songs) # returns both playlists


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
