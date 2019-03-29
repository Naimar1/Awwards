from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index, name='index'),
    # url(r'^$',views.profile,name = 'profile'),
    url(r'^$',views.timeline,name = 'timeline'),
    url(r'^comment/(\d+)', views.comment, name='comment'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^send/', views.send, name='send'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^upload/profile', views.upload_profile, name='upload_profile'),
    url(r'^upload_image/', views.upload_image, name='upload_image'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)