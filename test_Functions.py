from unittest import TestCase
import data
import Classes
import Functions
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

    def test_playlist_duration_1(self):
        songs = songs1
        total_time = data.Duration(3, 0)
        expected = [
            data.Song("HUMBLE.", data.Duration(2, 57), 2017, "Kendrick Lamar"),
            data.Song("Old Town Road", data.Duration(2, 37), 2019, "Lil Nas X"),
            data.Song("Stay", data.Duration(2, 21), 2021, "The Kid LAROI & Justin Bieber")]
        result = Functions.playlist_duration(songs, total_time)
        self.assertEqual(expected, result)

    def test_playlist_total_duration_limit(self):
        songs = songs1
        total_time = data.Duration(30, 30)
        expected = [data.Song("Bohemian Rhapsody", data.Duration(5, 55), 1975, "Queen"),
                    data.Song("Imagine", data.Duration(3, 3), 1971, "John Lennon"),
                    data.Song("Billie Jean", data.Duration(4, 54), 1982, "Michael Jackson"),
                    data.Song("Hey Jude", data.Duration(7, 11), 1968, "The Beatles"),
                    data.Song("Like a Rolling Stone", data.Duration(6, 13), 1965, "Bob Dylan")]
        result = Functions.playlist_total_duration_limit(songs, total_time)
        self.assertEqual(expected, result)


    def test_playlist_shuffle_songs(self):
        songs = songs1
        expected = {
    1: data.Song("Bad Guy", data.Duration(3, 14), 2019, "Billie Eilish"),
    2: data.Song("Imagine", data.Duration(3, 3), 1971, "John Lennon"),
    3: data.Song("Uptown Funk", data.Duration(4, 30), 2014, "Mark Ronson ft. Bruno Mars"),
    4: data.Song("Smells Like Teen Spirit", data.Duration(5, 1), 1991, "Nirvana"),
    5: data.Song("Stay", data.Duration(2, 21), 2021, "The Kid LAROI & Justin Bieber"),
    6: data.Song("Bohemian Rhapsody", data.Duration(5, 55), 1975, "Queen"),
    7: data.Song("Hey Jude", data.Duration(7, 11), 1968, "The Beatles"),
    8: data.Song("Old Town Road", data.Duration(2, 37), 2019, "Lil Nas X"),
    9: data.Song("Like a Rolling Stone", data.Duration(6, 13), 1965, "Bob Dylan"),
    10: data.Song("Radioactive", data.Duration(3, 6), 2012, "Imagine Dragons"),
    11: data.Song("Billie Jean", data.Duration(4, 54), 1982, "Michael Jackson"),
    12: data.Song("Drivers License", data.Duration(4, 2), 2021, "Olivia Rodrigo"),
    13: data.Song("Rolling in the Deep", data.Duration(3, 48), 2010, "Adele"),
    14: data.Song("Shape of You", data.Duration(3, 53), 2017, "Ed Sheeran"),
    15: data.Song("Can't Feel My Face", data.Duration(3, 35), 2015, "The Weeknd"),
    16: data.Song("Shake It Off", data.Duration(3, 39), 2014, "Taylor Swift"),
    17: data.Song("HUMBLE.", data.Duration(2, 57), 2017, "Kendrick Lamar"),
    18: data.Song("Take Me to Church", data.Duration(4, 2), 2013, "Hozier"),
    19: data.Song("Blinding Lights", data.Duration(3, 22), 2019, "The Weeknd"),
    20: data.Song("Lose Yourself", data.Duration(5, 26), 2002, "Eminem")
}
        result = Functions.playlist_shuffle_songs(songs)
        self.assertEqual(expected, result)

