from django.contrib import admin
from .models import User,Image,Profile,Comment,Follow

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
  
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)


