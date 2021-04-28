# import unittest
# from app.models import Comment,Pitch,User
# from app import db

# class PitchTest(unittest.TestCase):
#     '''
#     Test Class to test the behaviour of the Pitch class
#     '''

#     def tearDown(self):
#         Pitch.query.delete()
#         User.query.delete()
#         Comment.query.delete()



#     def setUp(self):
#         self.user_Mugera = User(username = 'Mugera',password = 'chicken', email = 'Mugera@ms.com', bio= "A good man",profile_pic_path="/home/photos/db.png")
#         self.new_pitch = Pitch(title='testing', pitch='this is the pitch',category="Production",user=self.user_Mugera)
#         self.new_comment=Comment(comment="great pitch",user=self.user_Mugera,pitch=self.new_pitch)


#     def test_check_instance_variables(self):
#         self.assertEquals(self.new_comment.comment,'great pitch')
#         self.assertEquals(self.new_comment.user,self.user_Mugera)
#         self.assertEquals(self.new_comment.pitch,self.new_pitch)


#     def test_save_comment(self):
#         self.new_comment.save_comment()
#         self.assertTrue(len(Comment.query.all()) > 0)
