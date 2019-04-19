import unittest
from app.models import Pitch, User

def setUp(self):
    # self.user_Shiko = User(username = 'Shiko',password = 'potato', email = 'shiko@gmail.com')
    self.new_Pitch = Pitch(author = self.user_Shiko, category_name='pick up lines',pitch ='I’m not a photographer, but I can picture me and you together.',PostedOn = '04/01/2019',upVote = 20, downVote = 2)

def test_instance(self):
    self.assertTrue(isinstance(self.new_Pitch, Pitch))

if __name__ == '__main__':
    unittest.main()
