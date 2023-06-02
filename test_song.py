from song import Song, Artist
import pytest

@pytest.fixture
def setup():
    artist = Artist("jose", "brasileiro", ["rock", "reggae"])
    song = Song("good morning", artist, "rock", 2023)
    yield song

def test_credits_artist_correctly(setup):
    song = setup
    assert(song.composer.name == "jose")

def test_number_of_streams_correctly_increased(setup):
    song = setup
    song.increase_number_of_streams(500)
    assert(song.number_of_streams == 500)
    song.increase_number_of_streams(100)
    assert(song.number_of_streams == 600)

def test_can_identify_hit_song(setup):
    song = setup
    song.increase_number_of_streams(2000000)
    assert(song.is_a_hit_song() == True)
    

