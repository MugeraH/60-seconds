import unittest
from app.models import Comment,Pitch,User
from app import db

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        self.user_Mugera = User(username='wiko', password='banana', email='wiko@ms.com')  
        self.new_pitch = Pitch(title='Humour',pitch="He who laughs last is the one who got the joke the last",category="Humour",user = self.user_Mugera)
        self.new_comment= Comment(comment="great pitch",user=self.user_Mugera,pitch=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Comment.query.delete()
        
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'great pitch')
        self.assertEquals(self.new_comment.user,self.user_Mugera)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)


    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)
