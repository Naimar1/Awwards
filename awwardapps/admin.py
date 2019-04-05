from django.contrib import admin
from .models import Project,Profile,Rating

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
  
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Rating)



