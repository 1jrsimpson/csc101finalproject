# Here is the list of Songs we will be sorting
from Classes import Song
from Classes import Duration

# Song list 1
songs1 = [
    Song("Bohemian Rhapsody", Duration(5, 55), 1975, "Queen"),
    Song("Imagine", Duration(3, 3), 1971, "John Lennon"),
    Song("Billie Jean", Duration(4, 54), 1982, "Michael Jackson"),
    Song("Hey Jude", Duration(7, 11), 1968, "The Beatles"),
    Song("Like a Rolling Stone", Duration(6, 13), 1965, "Bob Dylan"),
    Song("Smells Like Teen Spirit", Duration(5, 1), 1991, "Nirvana"),
    Song("Rolling in the Deep", Duration(3, 48), 2010, "Adele"),
    Song("Blinding Lights", Duration(3, 22), 2019, "The Weeknd"),
    Song("Shake It Off", Duration(3, 39), 2014, "Taylor Swift"),
    Song("HUMBLE.", Duration(2, 57), 2017, "Kendrick Lamar"),
    Song("Lose Yourself", Duration(5, 26), 2002, "Eminem"),
    Song("Bad Guy", Duration(3, 14), 2019, "Billie Eilish"),
    Song("Old Town Road", Duration(2, 37), 2019, "Lil Nas X"),
    Song("Drivers License", Duration(4, 2), 2021, "Olivia Rodrigo"),
    Song("Uptown Funk", Duration(4, 30), 2014, "Mark Ronson ft. Bruno Mars"),
    Song("Stay", Duration(2, 21), 2021, "The Kid LAROI & Justin Bieber"),
    Song("Shape of You", Duration(3, 53), 2017, "Ed Sheeran"),
    Song("Radioactive", Duration(3, 6), 2012, "Imagine Dragons"),
    Song("Take Me to Church", Duration(4, 2), 2013, "Hozier"),
    Song("Can't Feel My Face", Duration(3, 35), 2015, "The Weeknd")]

# Song list 2
songs2 = [
    Song("Hotel California", Duration(6, 30), 1976, "Eagles"),
    Song("Superstition", Duration(4, 26), 1972, "Stevie Wonder"),
    Song("I Will Always Love You", Duration(4, 31), 1992, "Whitney Houston"),
    Song("Wonderwall", Duration(4, 18), 1995, "Oasis"),
    Song("Mr. Brightside", Duration(3, 42), 2003, "The Killers"),
    Song("No Woman, No Cry", Duration(7, 8), 1975, "Bob Marley & The Wailers"),
    Song("Africa", Duration(4, 55), 1982, "Toto"),
    Song("Take On Me", Duration(3, 48), 1985, "a-ha"),
    Song("Seven Nation Army", Duration(3, 52), 2003, "The White Stripes"),
    Song("Creep", Duration(3, 58), 1992, "Radiohead"),
    Song("I Wanna Dance with Somebody", Duration(4, 52), 1987, "Whitney Houston"),
    Song("September", Duration(3, 35), 1978, "Earth, Wind & Fire"),
    Song("Let It Go", Duration(3, 44), 2013, "Idina Menzel"),
    Song("Happy", Duration(3, 53), 2013, "Pharrell Williams"),
    Song("All of Me", Duration(4, 30), 2013, "John Legend"),
    Song("Royals", Duration(3, 10), 2013, "Lorde"),
    Song("Counting Stars", Duration(4, 17), 2013, "OneRepublic"),
    Song("Somebody That I Used to Know", Duration(4, 4), 2011, "Gotye ft. Kimbra"),
    Song("Shallow", Duration(3, 36), 2018, "Lady Gaga & Bradley Cooper"),
    Song("Pompeii", Duration(3, 34), 2013, "Bastille")]

# Song list 1 in dictionary format
songs_dict = {
    "Bohemian Rhapsody": {"duration": (5, 55), "year": 1975, "artist": "Queen"},
    "Imagine": {"duration": (3, 3), "year": 1971, "artist": "John Lennon"},
    "Billie Jean": {"duration": (4, 54), "year": 1982, "artist": "Michael Jackson"},
    "Hey Jude": {"duration": (7, 11), "year": 1968, "artist": "The Beatles"},
    "Like a Rolling Stone": {"duration": (6, 13), "year": 1965, "artist": "Bob Dylan"},
    "Smells Like Teen Spirit": {"duration": (5, 1), "year": 1991, "artist": "Nirvana"},
    "Rolling in the Deep": {"duration": (3, 48), "year": 2010, "artist": "Adele"},
    "Blinding Lights": {"duration": (3, 22), "year": 2019, "artist": "The Weeknd"},
    "Shake It Off": {"duration": (3, 39), "year": 2014, "artist": "Taylor Swift"},
    "HUMBLE.": {"duration": (2, 57), "year": 2017, "artist": "Kendrick Lamar"},
    "Lose Yourself": {"duration": (5, 26), "year": 2002, "artist": "Eminem"},
    "Bad Guy": {"duration": (3, 14), "year": 2019, "artist": "Billie Eilish"},
    "Old Town Road": {"duration": (2, 37), "year": 2019, "artist": "Lil Nas X"},
    "Drivers License": {"duration": (4, 2), "year": 2021, "artist": "Olivia Rodrigo"},
    "Uptown Funk": {"duration": (4, 30), "year": 2014, "artist": "Mark Ronson ft. Bruno Mars"},
    "Stay": {"duration": (2, 21), "year": 2021, "artist": "The Kid LAROI & Justin Bieber"},
    "Shape of You": {"duration": (3, 53), "year": 2017, "artist": "Ed Sheeran"},
    "Radioactive": {"duration": (3, 6), "year": 2012, "artist": "Imagine Dragons"},
    "Take Me to Church": {"duration": (4, 2), "year": 2013, "artist": "Hozier"},
    "Can't Feel My Face": {"duration": (3, 35), "year": 2015, "artist": "The Weeknd"}}
