class Song:
    def __init__(self, title, artist, running_time):
        self.title = title
        self.artist = artist
        self.running_time = running_time

    def __str__(self):
        return f'{self.title} by {self.artist}'


the_way_make_me_feel = Song('The Way You Make Me Feel', 'Michael Jackson', 508)
surpestition = Song('Superstition', 'Stevie Wonder', 247)

print(the_way_make_me_feel)
print(surpestition)