from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    landing_page = models.ImageField(upload_to='landingpage/')
    description = HTMLField()
    link= models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
    def save_image(self):
    	self.save()
    
    def delete_image(self):
    	self.delete()

    def update_description(self,new_description):
    	self.description = new_description
    	self.save()

    @classmethod
    def get_images_by_user(cls,id):
        images = Project.objects.filter(user_id=id)
        return images

    @classmethod
    def get_images_by_id(cls,id):
        image = Project.objects.get(id = id)
        return image

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains = search_term)
        return project


class Profile(models.Model):
    username = models.CharField(default='User',max_length=30)
    imgprofl = models.ImageField(upload_to = "profile/",null=True)
    bio = models.TextField(default='',blank = True)
    name =models.CharField(max_length=100)
    email = models.EmailField() 

    def __str__(self):
        return self.name
    
    def save_profile(self):
    	self.save()

class Rating(models.Model):
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    grade = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)