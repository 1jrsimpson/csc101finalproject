from unittest import TestCase
import data
import Classes
import Functions
from Classes import Song
from Classes import Duration
from data import songs1
from data import songs2


class Test(TestCase):
    def test_playlist_oldvnew_1(self):
        songs = songs1
        expected = None
        result = Functions.playlist_oldvnew(songs)
        self.assertEqual(expected, result)

    def test_playlist_oldvnew_2(self):
        songs = songs2
        expected = None
        result = Functions.playlist_oldvnew(songs)
        self.assertEqual(expected, result)

    ###############################################################################################
# FUNCTION 2 SONG DURATION

    def test_playlist_duration_1(self):
        songs = songs1
        total_time = data.Duration(3, 0)
        expected = [
    Song("Imagine", Duration(3, 3), 1971, "John Lennon"),
    Song("Rolling in the Deep", Duration(3, 48), 2010, "Adele"),
    Song("Blinding Lights", Duration(3, 22), 2019, "The Weeknd"),
    Song("Shake It Off", Duration(3, 39), 2014, "Taylor Swift"),
    Song("HUMBLE.", Duration(2, 57), 2017, "Kendrick Lamar"),
    Song("Bad Guy", Duration(3, 14), 2019, "Billie Eilish"),
    Song("Old Town Road", Duration(2, 37), 2019, "Lil Nas X"),
    Song("Stay", Duration(2, 21), 2021, "The Kid LAROI & Justin Bieber"),
    Song("Shape of You", Duration(3, 53), 2017, "Ed Sheeran"),
    Song("Radioactive", Duration(3, 6), 2012, "Imagine Dragons"),
    Song("Can't Feel My Face", Duration(3, 35), 2015, "The Weeknd")
]

        result = Functions.playlist_duration(songs, total_time)
        self.assertEqual(expected, result)

    def test_playlist_duration_2(self):
        songs = songs2
        total_time = data.Duration(3, 0)
        expected = [
    Song("Mr. Brightside", Duration(3, 42), 2003, "The Killers"),
    Song("Take On Me", Duration(3, 48), 1985, "a-ha"),
    Song("Seven Nation Army", Duration(3, 52), 2003, "The White Stripes"),
    Song("Creep", Duration(3, 58), 1992, "Radiohead"),
    Song("September", Duration(3, 35), 1978, "Earth, Wind & Fire"),
    Song("Let It Go", Duration(3, 44), 2013, "Idina Menzel"),
    Song("Happy", Duration(3, 53), 2013, "Pharrell Williams"),
    Song("Royals", Duration(3, 10), 2013, "Lorde"),
    Song("Shallow", Duration(3, 36), 2018, "Lady Gaga & Bradley Cooper"),
    Song("Pompeii", Duration(3, 34), 2013, "Bastille")
]

        result = Functions.playlist_duration(songs, total_time)
        self.assertEqual(expected, result)

    ##############################################################################################
# FUNCTION 3 TOTAL DURATION

    def test_playlist_total_duration_limit_1(self):
        songs = songs1
        total_time = data.Duration(30, 30)
        expected = [Song("Bohemian Rhapsody", Duration(5, 55), 1975, "Queen"),
 Song("Imagine", Duration(3, 3), 1971, "John Lennon"),
 Song("Billie Jean", Duration(4, 54), 1982, "Michael Jackson"),
 Song("Hey Jude", Duration(7, 11), 1968, "The Beatles"),
 Song("Like a Rolling Stone", Duration(6, 13), 1965, "Bob Dylan")]
        result = Functions.playlist_total_duration_limit(songs, total_time)
        self.assertEqual(expected, result)

    def test_playlist_total_duration_limit_2(self):
        songs = songs2
        total_time = data.Duration(30, 30)
        expected = [
    Song("Hotel California", Duration(6, 30), 1976, "Eagles"),
    Song("Superstition", Duration(4, 26), 1972, "Stevie Wonder"),
    Song("I Will Always Love You", Duration(4, 31), 1992, "Whitney Houston"),
    Song("Wonderwall", Duration(4, 18), 1995, "Oasis"),
    Song("Mr. Brightside", Duration(3, 42), 2003, "The Killers")]

        result = Functions.playlist_total_duration_limit(songs, total_time)
        self.assertEqual(expected, result)

    ##############################################################################################
# FUNCTION 4 SHUFFLE
    def test_playlist_shuffle_songs_1(self):
        songs = songs1
        expected = len(songs)

        result = Functions.playlist_shuffle_songs(songs)
        self.assertEqual(expected, len(result))

    def test_playlist_shuffle_songs_2(self):
        songs = songs2
        expected = len(songs)

        result = Functions.playlist_shuffle_songs(songs)
        self.assertEqual(expected, len(result))
