# AI log: використала для пояснення помилок
class Playlist:
    def __init__(self, name):
        self.name = name
        # AttributeError: property 'duration' of 'PartyPlaylist' object has no setter
        # має getter, але не має setter, можна прочитати, але не можна присвоїти їй нове значення
       # self.duration = 0
        self._songs = []

    @property
    def name(self):
        return self._name
    # RecursionError: maximum recursion depth exceeded
    # self.name знову викликає getter name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Playlist name can't be empty")
        self._name = value

    @property
    def duration(self):
        return sum(seconds for _, seconds in self._songs)

    def add(self, title, seconds):
        self._songs.append((title, seconds))

class PartyPlaylist(Playlist):
    def first_song(self):
        return self._songs[0]
    # AttributeError: 'PartyPlaylist' object has no attribute '_PartyPlaylist__songs'. Did you mean: '_Playlist__songs'
    # __songs перетворює на _Playlist__songs, а дочірній клас шукав інший атрибут _PartyPlaylist__songs

p = PartyPlaylist("Friday")
p.add("Song A", 200)
p.add("Song B", 180)
print(p.name, p.duration)
print(p.first_song())