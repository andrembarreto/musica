from artist import Artist

class Song:
    def __init__(self, name: str, composer: Artist, genre: str, release_year: int) -> None:
        self.name = name
        self.composer = composer
        self.genre = genre
        self.release_year = release_year
        self.number_of_streams = 0

    def increase_number_of_streams(self, new_streams: int):
        self.number_of_streams += new_streams

    def is_a_hit_song(self) -> bool:
        return self.number_of_streams > 1000000