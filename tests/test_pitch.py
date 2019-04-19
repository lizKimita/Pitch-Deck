import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        # self.user_Shiko = User(username = 'Shiko',password = 'potato', email = 'shiko@gmail.com')
        self.new_pitch = Pitch(pitch ='I’m not a photographer, but I can picture me and you together.',postedOn = '04/01/2019')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

