from django import forms
from .models import Project,Profile,Rating
from django.contrib.auth.forms import AuthenticationForm

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['username','grade','imgprofl']
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']
class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']
       
class ProfileForm(forms.ModelForm):
   model = Profile
   username = forms.CharField(label='Username',max_length = 30)
	
   bio = forms.CharField(label='Image description',max_length=500)
   imgprofl = forms.ImageField(label = 'Image Field')


class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['grade','profile','project']
