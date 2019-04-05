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

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()
    projects=Project.objects.filter(username=current_user)

    return render(request,'profile.html',{"projects":projects,"profile":profile})

@login_required(login_url='/accounts/login/')
def site(request,site_id):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)

    try:
        project = Project.objects.get(id=site_id)
    except:
        raise ObjectDoesNotExist()

    try:
        ratings = Rating.objects.filter(project_id=site_id)
        design = Rating.objects.filter(project_id=site_id).values_list('design',flat=True)
        usability = Rating.objects.filter(project_id=site_id).values_list('usability',flat=True)
        content = Rating.objects.filter(project_id=site_id).values_list('content',flat=True)
        total_design=0
        total_usability=0
        total_content = 0
        print(design)
        for rate in design:
            total_design+=rate
        print(total_design)

        for rate in usability:
            total_usability+=rate
        print(total_usability)

        for rate in content:
            total_content+=rate
        print(total_content)

        grade=(total_design+total_content+total_usability)/3

        print(grade)

        project.design = total_design
        project.usability = total_usability
        project.content = total_content
        project.grade = grade

        project.save()

    except:
        return None

    if request.method =='POST':
        form = RatingForm(request.POST,request.FILES)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project= project
            rating.profile = profile
            rating.grade = (rating.design+rating.usability+rating.content)/2
            rating.save()
    else:
        form = RatingForm()

    return render(request,"site.html",{"project":project,"profile":profile,"ratings":ratings,"form":form})
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_landing_pages = Project.search_by_title(search_term)
        message=f"{search_term}"

        return render(request,'all-pages/search.html',{"message":message,"landing_pages":searched_landing_pages})

    else:
        message="nothing to display"
        return render(request,'all-pages/search.html',{"message":message})


