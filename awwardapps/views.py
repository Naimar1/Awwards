from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .forms import ProfileForm,ProjectForm,RatingForm,UploadImageForm,ProfileUploadForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from . models import Profile,Project,Rating
from django.contrib.auth.models import User
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    title = 'Awwards'
    image_posts = Project.objects.all()
    id=None
    for image in image_posts:
        id=image.id
        
   
    form = RatingForm()
    return render(request, 'index.html', {"title":title,"image_posts":image_posts,"form":form})

