from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index, name='index'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^new/project$',views.new_project, name='new-project'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^upload/profile', views.upload_profile, name='upload_profile'),
    url(r'^upload_image/', views.upload_image, name='upload_image'),
    url(r'^rating/(/i+)', views.rating, name='rating'),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view()),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)