
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^markdownx/', include('markdownx.urls')),
    ]
