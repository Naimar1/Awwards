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


