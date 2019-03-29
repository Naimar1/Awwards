from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class inkoko(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save() 

    class Meta:
        ordering = ['first_name']

class Image(models.Model):
    image = models.ImageField(upload_to = "pictures/",null = True)
    name = models.CharField(max_length = 30,null = True)
    caption = models.TextField(null = True)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User,null=True)

    def __str__(self):
    	return self.name

    def save_image(self):
    	self.save()
    
    def delete_image(self):
    	self.delete()

    def update_caption(self,new_caption):
    	self.caption = new_caption
    	self.save()

    @classmethod
    def get_images_by_user(cls,id):
        images = Image.objects.filter(user_id=id)
        return images

    @classmethod
    def get_images_by_id(cls,id):
        image = Image.objects.get(id = id)
        return image

    class Meta:
    	ordering = ['-pub_date']

    def save_profile(self):
    	self.save()

class Profile(models.Model):
    username = models.CharField(default='User',max_length=30)
    imgprofl = models.ImageField(upload_to = "profile/",null=True)
    bio = models.TextField(default='',blank = True) 

    def __str__(self):
        return self.username

    def delete_profile(self):
        self.delete()

    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(first_name__icontains = search_term)
        return profiles 

class Comment(models.Model):
    comment= models.TextField( blank=True)
    user = models.ForeignKey(User, null= True)
    image = models.ForeignKey(Image, null= True,related_name='comment')

    def __str__(self):
        return self.comment


    def delete_comment(self):
        self.delete()

    def save_comment(self):
        self.save()

class Follow(models.Model):
	user = models.ForeignKey(Profile,null=True)
	follower = models.ForeignKey(User,null=True)

	def __int__(self):
		return self.name

	def save_follower(self):
		self.save()

	def delete_follower(self):
		self.save()


   
