class Song:
    def __init__(self):
        title = ''
        artist = ''
        running_time = 0


backbone = Song()
backbone.title = 'Backbone'
backbone.artist = 'Gojira'
backbone.running_time = 259
anklebitters = Song()
anklebitters.title = 'Anklebiters'
anklebitters.artist = 'Paramore'
anklebitters.running_time = 168
only_exception = Song()
only_exception.title = 'Only Exception'
only_exception.artist = 'Paramore'
only_exception.running_time = 275

print(backbone.title)