import unittest
from app.models import Pitch,User
from app import db



class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''
          
    

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_Mugera = User(username = 'Sam',password = 'chklff', email = 'Mukkdkd@ms.com', bio= "A good man",profile_pic_path="/home/photos/db.png")
        
        
        self.new_pitch = Pitch(title='Humour',pitch="He who laughs last is the one who got the joke the last",category="Humour",user = self.user_Mugera)
   
    # def tearDown(self):
    #     Pitch.query.delete()
    #     User.query.delete()
  
    
    # We then check if the values of variables are correctly being placed.
    def test_check_instance_variables(self):
        
        self.assertEquals(self.new_pitch.title,'Humour')
        self.assertEquals(self.new_pitch.pitch,"He who laughs last is the one who got the joke the last")
        self.assertEquals(self.new_pitch.category,'Humour')
        self.assertEquals(self.new_pitch.user,self.user_Mugera)
       
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)
        
   
    def test_get_pitch_by_category(self):

        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitches("Humour")
        self.assertTrue(len(got_pitches) > 1)

 
