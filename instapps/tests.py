from django.test import TestCase
from .models import Profile,Image,Comment
import datetime as dt
# Create your tests here.

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.naimar= Profile(username ="naimar")

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.naimar,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.naimar.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new profile and saving it
        self.naimar= Profile(username ='naimar')
        self.naimar.save_profile()
        # Creating  new image
        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post',profile = self.naimar)
        self.new_image.save()

class CommentTestClass(TestCase):

    def setUp(self):
        
        self.new_comment = Comment(comment= "comment")
        self.new_comment.save()


    def tearDown(self):
        Profile.objects.all().delete()  
        comment.objects.all().delete()
        Image.objects.all().delete()
