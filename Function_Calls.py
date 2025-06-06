
# This is where we call our functions and show that they work
import Functions
import Classes
from Classes import Duration
import data
from data import songs_dict

# Calls for old vs new
my_playlists= Functions.playlist_oldvnew(data.songs1)

my_playlists2= Functions.playlist_oldvnew(data.songs2)


# Calls for shuffled songs
my_shuffled= Functions.playlist_shuffle_songs(data.songs1)


