from django.test import TestCase
from .models import Profile,Project,Rating
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
class ProjectTestClass(TestCase):

    def setUp(self):
        # Creating a new profile and saving it
        self.naimar= Profile(username ='naimar')
        self.naimar.save_profile()
        # Creating  new project
        self.new_project= Project(title = 'Gallery',post = 'This is for photo album',profile = self.naimar)
        self.new_project.save()

class RatingTestClass(TestCase):

    def setUp(self):
        
        self.new_rating = Rating(rating= "rating")
        self.new_rating.save()


    def tearDown(self):
        Profile.objects.all().delete()  
        Rating.objects.all().delete()
        Project.objects.all().delete()
