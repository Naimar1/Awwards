from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .forms import ProfileUploadForm,CommentForm,ProfileForm,UploadImageForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from . models import Image,Profile, User, Follow, Comment
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    title = 'Instagram'
    image_posts = Image.objects.all()
    id=None
    for image in image_posts:
        id=image.id
        # print(id)
    post = get_object_or_404(Image,id=id)
    # print(id)
    form = CommentForm()
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)

    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         # comment.user = current_user
    #         comment.user_id=current_user.id
    #         # comment.image = post
    #         comment.image_id=id
    #         comment.save()
    #         return redirect('index')
    # else:
        
    

    # print(image_posts)
    return render(request, 'index.html', {"title":title,"image_posts":image_posts, "form":form})


@login_required(login_url='/accounts/login/')
def comment(request,id):
    current_user = request.user
    users = User.objects.get(pk=current_user.id)
    images = Image.objects.get(pk=id)
    print(users)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = users
        #     # comment.user=users
        #     # comment.image = post
            comment.image=images
            comment.save()
        return redirect('index')
    else:
        return redirect('index')


@login_required(login_url='/accounts/login/')
def profile(request):
	 current_user = request.user
	 profile = Profile.objects.all()
	 follower = Follow.objects.filter(user = profile)

	 return render(request, 'profile.html',{"current_user":current_user,"profile":profile,"follower":follower})

@login_required(login_url='/accounts/login/')
def timeline(request):
	current_user = request.user 
	profile = Profile.objects.order_by('-time_uploaded')
	comment = Comment.objects.order_by('-time_comment')
	
	return render(request, 'all-pages/timeline.html',{"profile":profile,"comment":comment})

@login_required(login_url='/accounts/login/')
def one_img(request,image_id):
	image = image.objects.get(id= image_id)

	return render(request, 'all-pages/one_img.html',{"image":image})

@login_required(login_url='/accounts/login/')
def like(request,image_id):
	Image = Image.objects.get(id=image_id)
	like +=1
	save_like()
	return redirect(timeline)

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_profiles = Profile.search_by_imgprofl(search_term)
        message = f"{search_term}"

        return render(request, 'all-pages/search_image.html',{"message":message,"images": searched_profiles})

    else:
        message = "nothing to display"
        return render(request, 'all-pages/search_image.html',{"message":message})

@login_required(login_url='/accounts/login/')
def upload_image(request):
    current_user = request.user
    title = 'Image'
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user_key = current_user
            image.save()
        
    else:
        form = UploadImageForm()
    return render(request, 'all-pages/upload_image.html', {"form": form,"current_user":current_user,"title":title})


@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.imgprofl = form.cleaned_data['imgprofl']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(imgprofl = form.cleaned_data['imgprofl'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()


    return render(request,'upload_profile.html',{"title":title,"current_user":current_user,"form":form})


@login_required(login_url='/accounts/login/')
def send(request):
    '''
    View function that displays a forms that allows users to upload images
    '''
    current_user = request.user

    if request.method == 'POST':

        form = ImageForm(request.POST ,request.FILES)

        if form.is_valid():
            image = form.save(commit = False)
            image.user_key = current_user
            image.likes +=0
            image.save() 

            return redirect( timeline)
    else:
        form = ImageForm() 
    return render(request, 'all-pages/send.html',{"form" : form}) 