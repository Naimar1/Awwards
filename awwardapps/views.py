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

@login_required(login_url='/accounts/login/')
def rating(request,id):
    current_user = request.user
    users = User.objects.get(pk=current_user.id)
    landing_pages = Project.objects.get(id=id)
    print(users)
    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            rating = form.save(commit=False)
            ratingt.user = users
       
            rating.landing_page=landing_pages
            rating.save()
        return redirect('index')
    else:
        return redirect('index') 

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('Index')
    else:
        form=ProfileForm()

    return render(request,'create_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.username = current_user
            project.imgprofl = profile.imgprofl
            
            project.save()
    else:
        form = ProjectForm()

    return render(request,'new_project.html',{"form":form})


