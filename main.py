

class Artist:
    def _init_(self, name):
        self.name = name


class Albumb:
    def _init_(self, title, artist):
        self.title = title
        self.artist = artist


class Songs:
    def _init_(self, Songs):
        self.Songs = Songs


class Artist:
    def _init_(self, name):
        self.name = name


class Playlist:
    def _init_(self, name):
        self.name = name
        self.songs = []  # construct list for songs

        def addSong(self, song):
            self.songs.append(song)  # add song to songs
