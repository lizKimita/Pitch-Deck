class Pitch:
    '''
    Pitch class to define the Pitch Objects
    '''
    all_pitches = []

    def __init__(self, author, category_name, pitch, PostedOn, upVote, downVote):
        self.author = author
        self.category_name = category_name
        self.pitch = pitch
        self.PostedOn = PostedOn
        self.upVote = upVote
        self.downVote = downVote

    def save_pitch(self):
        Pitch.all_pitches.append(self)

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

# class User: