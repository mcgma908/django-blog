from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
    #/
    url(r'^$', views.blog_home, {'page': 1}),
    #/page/2/
    url(r'^page/(?P<page>\d+)/$', views.blog_home, name='blog_home'),    
    #/2017/this-is-my-first-post/
    url(r'^(?P<year>[0-9]{4})/(?P<page_slug>[\w-]+)/$', views.blog_single, name='blog_single'),
    #/about
    url(r'^about/$', views.about, name='about'),
    #/archive
    url(r'^archive/$', views.archive, name='archive'),
    #/archive/2017     Make sure its above /archive/problem-solving !!!
    url(r'^archive/(?P<year>[0-9]{4})/$', views.year_archive, name='year_archive'),    
    #/archive/problem-solving
    url(r'^archive/(?P<tag_slug>[\w-]+)/$', views.single_archive, name='single_archive'),
    #/further-reading
    url(r'^further-reading/$', views.further, name='further'),  
       ]

