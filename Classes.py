# This file includes or Class Definitions

# Class Song
class Song:
    # Below are the dunder functions that describe this class
    # Initialize a new Song object.
    # input: the song's artist as a string
    # input: the song's title as a string
    # input: the song's duration as a Duration object
    # input: the year the song was released
    def __init__(self, title: str, duration: float, year_released: int, artist: str):
        self.title = title
        self.duration = duration
        self.year_released = year_released
        self.artist = artist
    # Define the string representation of the class
    def __str__(self):
        return 'Song title: {}, Song duration: {}, Release year: {}, Song artist: {}'.format(self.title, self.duration, self.year_released, self.artist)

    # Provide a developer-friendly string representation of the object.
    # input: Song for which a string representation is desired.
    # output: string representation
    def __repr__(self):
        return 'Song({}, {}, {})'.format(self.title, self.duration, self.year_released, self.artist)

    # Compare the Song object with another value to determine equality.
    # input: Song against which to compare
    # input: Another value to compare to the Song
    # output: boolean indicating equality
    def __eq__(self,other):
        return (self is other and type(other) == type(self) and
                ((other.title) == (self.title)) and ((other.duration) == (self.duration)) and
                ((other.year_released) == (self.year_released)) and ((other.artist) == (self.artist)))

# Class Duration
# Representation of a duration as minutes and seconds.
class Duration:
    # Initialize a new Duration object.
    # input: minutes as an integer
    # input: seconds as an integer
    def __init__(self, minutes:int, seconds: int):
        self.minutes = minutes
        self.seconds = seconds


    # Provide a developer-friendly string representation of the object.
    # input: Duration for which a string representation is desired.
    # output: string representation
    def __repr__(self) -> str:
        return 'Duration({}, {})'.format(self.minutes, self.seconds)


    # Compare the Duration object with another value to determine equality.
    # input: Duration against which to compare
    # input: Another value to compare to the Duration
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Duration and
                self.minutes == other.minutes and
                self.seconds == other.seconds)